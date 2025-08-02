async function sendMessage() {
    try {
        const username = document.getElementById('username').value || 'Anonymous';
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();
        
        if (!message) return;
        
        const response = await fetch('/send_message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, message })
        });

        if (!response.ok) {
            throw new Error('Failed to send message');
        }
        
        messageInput.value = '';
        await fetchMessages();
    } catch (error) {
        console.error('Error sending message:', error);
        alert('Failed to send message. Please try again.');
    }
}

async function fetchMessages() {
    try {
        const response = await fetch('/get_messages');
        if (!response.ok) {
            throw new Error('Failed to fetch messages');
        }
        
        const messages = await response.json();
        const chatLog = document.getElementById('chatLog');
        
        chatLog.innerHTML = '';
        messages.forEach(msg => {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${msg.username === (document.getElementById('username').value || 'Anonymous') ? 'sent' : 'received'}`;
            messageDiv.innerHTML = `
                <div class="username">${msg.username}</div>
                <div>${msg.message}</div>
                <div class="timestamp">${new Date(msg.timestamp).toLocaleTimeString()}</div>
            `;
            chatLog.appendChild(messageDiv);
        });
        
        chatLog.scrollTop = chatLog.scrollHeight;
    } catch (error) {
        console.error('Error fetching messages:', error);
        const chatLog = document.getElementById('chatLog');
        if (!chatLog.querySelector('.error-message')) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = 'Failed to load messages. Please refresh the page.';
            chatLog.prepend(errorDiv);
        }
    }
}

// Poll for new messages every 2 seconds
setInterval(fetchMessages, 2000);

// Initial fetch
fetchMessages();

// PWA service worker registration
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/sw.js')
        .then(reg => console.log('Service Worker registered', reg))
        .catch(err => console.log('Service Worker registration failed', err));
}