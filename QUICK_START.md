# 🎃 Quick Start Guide - Get Running in 5 Minutes!

## Step 1: Install Requirements (2 minutes)

Open Command Prompt or PowerShell in this folder and run:

```bash
pip install -r requirements.txt
```

## Step 2: Start the Server (1 minute)

**Option A - Double-click:**
- Just double-click `start_contest.bat`

**Option B - Command line:**
```bash
python app.py
```

You should see:
```
🎃 HALLOWEEN COSTUME CONTEST APP 🎃
Starting server...
Access the app at:
  → http://localhost:5000
```

## Step 3: Generate QR Code (1 minute)

In another terminal:
```bash
python generate_qr.py
```

This creates `contest_qr_code.png` - print or display this at your party!

## Step 4: Test It (1 minute)

1. Open your browser to `http://localhost:5000`
2. Click "Enter the Contest"
3. Submit a test entry
4. Go back and click "Vote" 
5. Vote for your test entry
6. Check "Results" to see it appear

## That's It! 🎉

Your contest app is ready. Just:
- Display the QR code
- Keep your computer on
- Let guests scan and participate!

---

## Quick Troubleshooting

**"pip not found"**
- Make sure Python is installed: `python --version`
- Try: `python -m pip install -r requirements.txt`

**"Port 5000 already in use"**
- Edit `app.py`, change `port=5000` to `port=5001`

**Can't access from phone**
- Check both devices are on same WiFi
- Use the IP address shown in terminal, not "localhost"

**Need to reset the contest?**
- Stop the server (Ctrl+C)
- Delete `contest_data.json`
- Delete the `uploads` folder
- Start again

---

## During Your Party

**To keep running smoothly:**
1. ✅ Keep your computer plugged in
2. ✅ Disable sleep/hibernation mode
3. ✅ Keep the terminal window open
4. ✅ Note the URL to tell guests

**To stop the server:**
- Press `Ctrl+C` in the terminal

**To restart:**
- Run `python app.py` again (all data is saved!)

---

## Party Checklist

- [ ] Install requirements
- [ ] Test the app
- [ ] Generate QR code
- [ ] Print QR code or prepare to display it
- [ ] Test accessing from your phone
- [ ] Disable computer sleep mode
- [ ] Plug in computer
- [ ] Note the URL for guests
- [ ] Have fun! 🎃

---

**Questions?** Check `README.md` for full documentation!


