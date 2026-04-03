const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// In‑memory storage (max 10 messages, newest first)
let messagesStore = [];

function addMessage(name, email, message) {
    const newMsg = {
        id: Date.now() + Math.random().toString(36).substring(2, 8),
        name: (name || 'Anonymous').trim().substring(0, 64),
        email: (email || 'no-email@provided').trim().substring(0, 100),
        message: (message || '(empty message)').trim().substring(0, 500),
        timestamp: new Date().toISOString()
    };
    messagesStore.unshift(newMsg);
    if (messagesStore.length > 10) messagesStore = messagesStore.slice(0, 10);
    return newMsg;
}

// Webhook endpoint – accepts name, email, message
app.post('/api/messages', (req, res) => {
    const { name, email, message } = req.body;
    const saved = addMessage(name, email, message);
    console.log(`📨 New message from ${saved.name} (${saved.email})`);
    res.status(201).json({ success: true, data: saved });
});

// Get all messages
app.get('/api/messages', (req, res) => {
    res.json(messagesStore);
});

// Delete a single message by ID
app.delete('/api/messages/:id', (req, res) => {
    const id = req.params.id;
    const initialLength = messagesStore.length;
    messagesStore = messagesStore.filter(msg => msg.id !== id);
    if (messagesStore.length === initialLength) {
        return res.status(404).json({ error: 'Message not found' });
    }
    console.log(`🗑️ Deleted message with id ${id}`);
    res.json({ success: true, message: 'Message deleted' });
});

// Clear all messages (instructor utility)
app.delete('/api/messages', (req, res) => {
    messagesStore = [];
    console.log('🧹 All messages cleared');
    res.json({ success: true });
});

// Serve the frontend dashboard
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'dashboard.html'));
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`
╔══════════════════════════════════════════════════════╗
║   🚀 Webhook server running                           ║
║   👉 Instructor dashboard: http://localhost:${PORT}    ║
║   🔗 POST webhook: http://localhost:${PORT}/api/messages ║
║   ❌ DELETE single: /api/messages/:id                 ║
║   📦 Max 10 messages (oldest auto‑removed)           ║
╚══════════════════════════════════════════════════════╝
    `);
});