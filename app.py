from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import hashlib
from cryptography.fernet import Fernet
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
uri = os.environ.get('MONGODB_URI')
if not uri:
    raise ValueError("MONGODB_URI environment variable is not set")

try:
    client = MongoClient(uri, server_api={'version': '1', 'strict': True, 'deprecation_errors': True})
    # Verify the connection
    client.admin.command('ping')
    db = client['chat_app']
    messages_collection = db['messages']
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")
    raise

# Encryption setup
key = os.environ.get('ENCRYPTION_KEY')
if not key:
    key = Fernet.generate_key()
    print("Warning: ENCRYPTION_KEY not set, using temporary key")
cipher = Fernet(key if isinstance(key, bytes) else key.encode())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        username = data.get('username', 'Anonymous')
        message = data.get('message')
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Encrypt the message
        encrypted_message = cipher.encrypt(message.encode()).decode()
        
        # Store message in MongoDB
        message_doc = {
            'username': username,
            'message': encrypted_message,
            'timestamp': datetime.utcnow()
        }
        
        messages_collection.insert_one(message_doc)
        return jsonify({'status': 'success'})
        
    except Exception as e:
        print(f"Error in send_message: {str(e)}")
        return jsonify({'error': 'Failed to process message'}), 500

@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        messages = list(messages_collection.find().sort('timestamp', -1).limit(50))
        decrypted_messages = []
        
        for msg in messages:
            try:
                decrypted_message = cipher.decrypt(msg['message'].encode()).decode()
                decrypted_messages.append({
                    'username': msg['username'],
                    'message': decrypted_message,
                    'timestamp': msg['timestamp'].isoformat()
                })
            except Exception as e:
                print(f"Error decrypting message: {str(e)}")
                continue
                
        return jsonify(decrypted_messages)
    except Exception as e:
        print(f"Error in get_messages: {str(e)}")
        return jsonify({'error': 'Failed to retrieve messages'}), 500

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@app.route('/health')
def health_check():
    try:
        # Check MongoDB connection
        client.admin.command('ping')
        return jsonify({
            'status': 'healthy',
            'mongodb': 'connected'
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

# This is for local development
if __name__ == '__main__':
    app.run(debug=True)