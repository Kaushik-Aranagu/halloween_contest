# 🏗️ Architecture Overview

This document explains how the Halloween Costume Contest app works behind the scenes.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        YOUR COMPUTER                         │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │              Flask Web Server (app.py)             │    │
│  │                   Port 5000                        │    │
│  │                                                     │    │
│  │  Routes:                                           │    │
│  │    GET  /            → index.html                  │    │
│  │    GET  /participate → participate.html            │    │
│  │    GET  /vote        → vote.html                   │    │
│  │    GET  /results     → results.html                │    │
│  │    POST /api/submit  → Save entry                  │    │
│  │    POST /api/vote    → Record vote                 │    │
│  │    GET  /api/entries → Get all entries             │    │
│  └────────────────────────────────────────────────────┘    │
│                          ↓  ↑                               │
│  ┌────────────────────────────────────────────────────┐    │
│  │               Data Storage                          │    │
│  │                                                     │    │
│  │  • contest_data.json (entries & votes)             │    │
│  │  • uploads/ (costume photos)                       │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              ↑
                              │ WiFi Network
                              │
        ┌─────────────┬───────┴────────┬─────────────┐
        │             │                │             │
    ┌───────┐    ┌───────┐        ┌───────┐    ┌───────┐
    │📱Phone│    │💻 Tab │        │📱Phone│    │💻 Tab │
    │       │    │       │        │       │    │       │
    │Guest 1│    │Guest 2│        │Guest 3│    │Guest 4│
    └───────┘    └───────┘        └───────┘    └───────┘
```

## Data Flow

### 1. Submitting an Entry

```
User's Browser                Flask Server              Storage
─────────────                ──────────────            ─────────
    │                              │                        │
    │  POST /api/submit            │                        │
    │  (form data + photo)         │                        │
    ├─────────────────────────────>│                        │
    │                              │                        │
    │                              │ Save photo to          │
    │                              │ uploads/               │
    │                              ├───────────────────────>│
    │                              │                        │
    │                              │ Add entry to           │
    │                              │ contest_data.json      │
    │                              ├───────────────────────>│
    │                              │                        │
    │  <── Success Response ───────┤                        │
    │  {success: true}             │                        │
```

### 2. Voting

```
User's Browser                Flask Server              Storage
─────────────                ──────────────            ─────────
    │                              │                        │
    │  POST /api/vote              │                        │
    │  {entry_id, voter_id}        │                        │
    ├─────────────────────────────>│                        │
    │                              │                        │
    │                              │ Check existing votes   │
    │                              │ Remove old vote        │
    │                              │ Add new vote           │
    │                              ├───────────────────────>│
    │                              │                        │
    │  <── Success Response ───────┤                        │
```

### 3. Viewing Results

```
User's Browser                Flask Server              Storage
─────────────                ──────────────            ─────────
    │                              │                        │
    │  GET /api/entries            │                        │
    ├─────────────────────────────>│                        │
    │                              │                        │
    │                              │ Read contest_data.json │
    │                              │<───────────────────────┤
    │                              │                        │
    │                              │ Calculate vote counts  │
    │                              │                        │
    │  <── JSON with entries ──────┤                        │
    │  + vote counts               │                        │
```

## File Structure

```
halloween_contest/
│
├── app.py                    # Main Flask application
│   ├── Routes for pages
│   ├── API endpoints
│   └── File upload handling
│
├── templates/                # HTML pages
│   ├── index.html           # Landing page
│   ├── participate.html     # Entry submission form
│   ├── vote.html           # Voting interface
│   └── results.html        # Results dashboard
│
├── uploads/                 # Uploaded costume photos
│   └── (created at runtime)
│
├── contest_data.json        # Database (JSON file)
│   └── (created at runtime)
│
├── generate_qr.py          # QR code generator utility
├── check_setup.py          # Setup verification script
├── requirements.txt        # Python dependencies
├── start_contest.bat       # Windows startup script
│
└── Documentation
    ├── README.md           # Main documentation
    ├── QUICK_START.md      # Getting started guide
    ├── OPTIONS.md          # Alternative implementations
    └── ARCHITECTURE.md     # This file
```

## Data Structure

### contest_data.json

```json
{
  "entries": [
    {
      "id": "1",
      "name": "John Doe",
      "costume_name": "Vampire Lord",
      "description": "Classic vampire with a twist!",
      "photo": "20241031_123456_costume.jpg",
      "timestamp": "2024-10-31T12:34:56.789"
    }
  ],
  "votes": {
    "1": ["alice", "bob", "charlie"],
    "2": ["alice"]  // Alice changed vote from entry 1 to 2
  },
  "settings": {
    "show_votes": true,
    "voting_enabled": true
  }
}
```

## Frontend Architecture

Each HTML page is self-contained with:

1. **HTML Structure** - Page layout and forms
2. **CSS Styling** - Embedded styles (no external CSS files needed)
3. **JavaScript** - Client-side logic for:
   - Form submission via Fetch API
   - Dynamic content loading
   - Real-time updates
   - User feedback

### Key JavaScript Patterns

**Fetch API for async requests:**
```javascript
const response = await fetch('/api/submit', {
    method: 'POST',
    body: formData
});
const data = await response.json();
```

**Auto-refresh for live updates:**
```javascript
// Refresh entries every 30 seconds
setInterval(loadEntries, 30000);
```

**Local storage for voter ID:**
```javascript
// Remember voter between page loads
localStorage.setItem('voterId', currentVoterId);
```

## Security Considerations

### Current Implementation (Designed for trusted environment)

✅ **Implemented:**
- File size limits (16MB)
- File type validation (images only)
- Secure filename handling
- One vote per voter ID
- Input sanitization (via secure_filename)

⚠️ **Not Implemented (intentionally):**
- Authentication (not needed for party)
- Rate limiting (small group)
- HTTPS (local network only)
- Password protection (trusted environment)

### For Public Deployment

If you wanted to deploy this publicly, you would need to add:
- User authentication
- HTTPS/SSL
- Rate limiting
- CSRF protection
- Admin authentication
- IP-based restrictions
- Database instead of JSON file

## Performance Characteristics

### Suitable For:
- ✅ 1-30 simultaneous users
- ✅ 1-50 total entries
- ✅ 1-500 total votes
- ✅ Photos up to 16MB
- ✅ Single evening duration

### May Struggle With:
- ❌ 50+ simultaneous users
- ❌ 100+ entries
- ❌ Thousands of votes
- ❌ Multi-day high traffic

### Bottlenecks:
1. **JSON file I/O** - Every vote writes entire file
2. **No caching** - Data loaded from disk each request
3. **Single threaded** - Flask development server limitation

### If You Need to Scale:
1. Switch to SQLite or PostgreSQL database
2. Add Redis for caching
3. Use production WSGI server (Gunicorn)
4. Add load balancer for multiple instances
5. Use CDN for image serving

But for your party? The current implementation is perfect! 🎃

## Extending the App

### Easy Modifications:

**Add a countdown timer:**
```javascript
// In results.html or vote.html
const deadline = new Date('2024-10-31T23:59:59');
// Display countdown
```

**Add categories:**
```python
# In app.py entry structure
"category": "Scariest"  # Scariest, Funniest, Most Creative
```

**Export results to CSV:**
```python
import csv
# Add route to export data
```

**Add multiple photos per entry:**
```python
# Modify form to accept multiple files
photos = request.files.getlist('photos')
```

### Moderate Modifications:

- Email notifications
- SMS voting
- Social media integration
- Admin dashboard
- Voting analytics

### Complex Modifications:

- Real-time websockets
- Video uploads
- Live streaming results
- Machine learning for auto-categorization

## Technology Choices Explained

**Why Flask?**
- Lightweight
- Easy to learn
- Perfect for small apps
- Great documentation
- Python ecosystem

**Why JSON storage?**
- Simple
- No database setup
- Human-readable
- Easy to backup/restore
- Perfect for small data

**Why embedded CSS/JS?**
- Self-contained files
- No build process
- Easy to understand
- No external dependencies
- Simple deployment

**Why no database?**
- Adds complexity
- Overkill for <50 entries
- JSON is sufficient
- Easier troubleshooting
- No migrations needed

## Questions?

If you want to understand or modify any part of the system, check the code comments or refer to the relevant documentation file!

**Happy coding!** 🎃👻


