#!/usr/bin/env python3
"""
Test MongoDB connection
"""
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

# Your MongoDB URI
uri = "mongodb+srv://muhammednihal24ag039:l6ZrDiiOk3TY74aV@cluster0.pppmmcf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

print(f"Testing connection to MongoDB Atlas...")

try:
    # Add timeout to prevent hanging
    client = MongoClient(
        uri, 
        server_api=ServerApi('1'),
        serverSelectionTimeoutMS=5000,  # 5 second timeout
        connectTimeoutMS=5000
    )
    
    print("Attempting to ping MongoDB...")
    client.admin.command('ping')
    print("✅ MongoDB connection successful!")
    
    # Test database operations
    db = client['chat_app']
    collection = db['messages']
    print("✅ Database and collection accessible!")
    
    # Test a simple operation
    count = collection.count_documents({})
    print(f"✅ Current message count: {count}")
    
except Exception as e:
    print(f"❌ Connection failed: {str(e)}")
    print("Possible issues:")
    print("1. Network connectivity issues")
    print("2. IP address not whitelisted in MongoDB Atlas")
    print("3. Incorrect username/password")
    print("4. Cluster is paused or unavailable")
