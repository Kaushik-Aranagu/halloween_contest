# 🎃 Halloween Costume Contest App

A simple, beautiful web application to manage your Halloween costume contest with photo uploads and voting!

## Features

✨ **Easy to Use** - Simple web interface accessible from any device  
📸 **Photo Uploads** - Participants can upload their costume photos  
🗳️ **Voting System** - Fair voting where each person can vote once (and change their vote)  
📊 **Live Results** - See rankings update in real-time  
👻 **Beautiful UI** - Modern, festive design perfect for Halloween  
📱 **Mobile Friendly** - Works great on phones and tablets  
🔒 **Privacy Friendly** - All data stored locally, no external services required

## Quick Start

### 🌐 Option A: Cloud Deployment (Recommended for parties!)

**Deploy to the cloud in 5 minutes** - no need to keep your computer running!

**Best for:** Guests not on same WiFi, better performance, no local PC needed

👉 **[See DEPLOY_CLOUD.md for complete cloud deployment guide](DEPLOY_CLOUD.md)**

**Quick Deploy to Render.com:**
1. Push code to GitHub
2. Sign up at render.com
3. Click "New Web Service" → Connect your repo
4. Deploy! (Takes 5 minutes)

Your contest will be live at `https://your-app.onrender.com` 🎉

---

### 💻 Option B: Run Locally

**Best for:** Testing, or if everyone is on same WiFi

#### Prerequisites

- Python 3.7 or higher installed on your computer
- WiFi network for guests to connect to

#### Installation

1. **Open a terminal/command prompt** and navigate to this folder:
   ```bash
   cd K:\p4\halloween_contest
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

#### Running the App

1. **Start the server:**
   ```bash
   python app.py
   ```

2. **Access the app:**
   - On your computer: Open `http://localhost:5000`
   - On other devices: Use your computer's IP address (shown when you start the app)

3. **Generate a QR code** (optional but recommended):
   ```bash
   python generate_qr.py
   ```
   This creates a QR code image that guests can scan to access the contest!

## How to Use at Your Party

### Setup (Before the Party)

1. Start the app on your computer
2. Generate the QR code and print it or display it
3. Test it by accessing the URL from your phone
4. Make sure your computer stays on and connected to WiFi during the party

### During the Party

**For Participants:**
1. Scan the QR code or visit the URL
2. Click "Enter the Contest"
3. Fill in name, costume name, description
4. Upload a photo
5. Submit!

**For Voters:**
1. Scan the QR code or visit the URL
2. Click "Vote for Your Favorite"
3. Enter your name
4. Browse all entries and click "Vote" on your favorite
5. You can change your vote anytime!

**For Viewing Results:**
1. Click "View Results" from the home page
2. See the top 3 on the podium
3. View all entries ranked by votes
4. Toggle "Show Vote Counts" to hide/show current votes

## Pages Overview

### Home Page (`/`)
Landing page with three options:
- 📸 Enter the Contest
- 🗳️ Vote for Your Favorite
- 🏆 View Results

### Participate Page (`/participate`)
Form for submitting contest entries:
- Name
- Costume name
- Description (optional)
- Photo upload

### Vote Page (`/vote`)
View all entries and vote:
- Enter your name to vote
- Browse all costume entries
- Click to vote for your favorite
- Change your vote anytime

### Results Page (`/results`)
See contest standings:
- Top 3 on podium with medals
- Full rankings of all entries
- Toggle to show/hide vote counts
- Auto-refreshes every 15 seconds

## Admin Features

### Toggle Vote Visibility
On the Results page, you can toggle whether vote counts are visible to everyone. This is useful if you want to:
- Hide votes during the contest to avoid bias
- Show votes at the end to announce winners

### Data Management
All data is stored in:
- `contest_data.json` - Entries and votes
- `uploads/` - Uploaded photos

To reset the contest, simply delete these files/folders.

## Tips for a Smooth Contest

1. **Test First** - Run through the whole process before the party
2. **Keep Computer Awake** - Disable sleep mode on your computer
3. **Good WiFi** - Make sure your WiFi can handle all your guests
4. **Charge Up** - Keep your computer plugged in
5. **Backup** - The `contest_data.json` file contains all data if you need to back it up

## Troubleshooting

**Can't access from phone?**
- Make sure both devices are on the same WiFi network
- Check if your computer's firewall is blocking port 5000
- Try using your computer's IP address instead of localhost

**Photos not uploading?**
- Check file size (max 16MB)
- Ensure file is an image format (jpg, png, gif, webp)
- Try a different browser

**Votes not counting?**
- Make sure voter entered their name
- Check if voting is enabled (it should be by default)
- Try refreshing the page

**Port 5000 already in use?**
Edit `app.py` and change the port number in the last line:
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Changed from 5000 to 5001
```

## Technical Details

- **Backend:** Flask (Python)
- **Frontend:** Vanilla HTML/CSS/JavaScript
- **Storage:** JSON file + local filesystem
- **Perfect for:** Small parties (<30 people)

## Security Notes

This app is designed for trusted environments (your home party). It:
- Doesn't require passwords or authentication
- Stores data locally on your computer
- Is accessible to anyone on your network
- Should not be exposed to the public internet

## Future Enhancements (Optional)

If you want to modify the app, here are some ideas:
- Add categories (Scariest, Funniest, Most Creative)
- Allow multiple photos per entry
- Add a timer/countdown for contest deadline
- Export results to PDF
- Add admin password for settings
- Social media sharing

## License

Free to use and modify for your party! Have a spooktacular time! 👻🎃

## Support

If you run into issues:
1. Check the troubleshooting section above
2. Make sure all requirements are installed
3. Check the terminal/console for error messages
4. Restart the server

---

**Happy Halloween!** 🎃👻🦇🕷️🍬


