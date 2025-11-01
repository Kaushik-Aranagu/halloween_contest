# 🧪 Test Locally & 🚀 Deploy to Railway

## Part 1: Testing Locally (15 minutes)

### Step 1: Install Dependencies

Open PowerShell or Command Prompt in the `halloween_contest` folder:

```bash
cd K:\p4\halloween_contest

# Install requirements
pip install -r requirements.txt
```

### Step 2: Start the Server

```bash
python app.py
```

You should see:
```
🎃 HALLOWEEN COSTUME CONTEST APP 🎃
====================================
Starting server...
Access the app at:
  → http://localhost:5000
```

### Step 3: Open in Browser

Open your browser to: **http://localhost:5000**

---

## 🧪 Testing Checklist

### Test 1: Home Page
- [ ] Home page loads
- [ ] See 4 buttons: Enter, Vote, Results, Admin
- [ ] All links work

### Test 2: Multiple Photo Upload

1. **Click "Enter the Contest"**
2. **Fill in the form:**
   - Name: Test User
   - Costume: Test Vampire
   - Description: Testing multiple photos
3. **Upload 3 photos:**
   - Click "Choose Files"
   - Hold Ctrl and select 3 different images
   - Should show "✅ 3 photos selected"
   - See all 3 photos previewed
4. **Submit**
   - Should redirect to home page
   - See success message

### Test 3: Photo Carousel

1. **Click "Vote for Your Favorite"**
2. **Check the entry you just created:**
   - Should see photo carousel with arrows
   - Click **►** arrow - should show photo 2
   - Click **►** again - should show photo 3
   - Click **◄** arrow - should go back to photo 2
   - Indicator dots should update
   - Prev button disabled on first photo
   - Next button disabled on last photo

### Test 4: Voting

1. **Enter your name** in the voter ID field
2. **Click "Vote 👍"** on your test entry
3. **Should see:** "Vote submitted successfully! Redirecting..."
4. **Should redirect to home page**

### Test 5: Results Page

1. **Click "View Results"**
2. **Check:**
   - Your entry appears
   - Vote count shows (if votes visible)
   - Photos display correctly
   - Carousel works here too

### Test 6: Admin Dashboard

1. **Go back to home**
2. **Click "🔧 Admin Dashboard"** at bottom
3. **Check statistics:**
   - Total Entries: 1
   - Total Votes: 1
   - Total Photos: 3 (the 3 you uploaded)
4. **Test downloads:**
   - Click "Download JSON Backup"
   - File should download: `contest_data_TIMESTAMP.json`
   - Open it - should see your entry data
5. **Test CSV export:**
   - Click "Export to CSV"
   - File should download: `contest_results_TIMESTAMP.csv`
   - Open in Excel - should see your entry

### Test 7: Automatic Backup

1. **Check backups folder:**
   ```bash
   dir backups
   # or
   ls backups/
   ```
2. **Should see:** `contest_backup_TIMESTAMP.json`
3. **Submit another entry** with 2 photos
4. **Check backups folder again:**
   - Should now have 2 backup files
   - Each with different timestamp

### Test 8: Multiple Entries

1. **Create 2-3 more test entries:**
   - Mix of 1, 2, 3, 4, 5 photos each
   - Different names and costumes
2. **Vote on different entries:**
   - Change your vote
   - Check vote count updates
3. **Test carousel on all entries:**
   - Single photo entries show normal image
   - Multi-photo entries show carousel

---

## ✅ Local Testing Complete!

If all tests pass, you're ready to deploy to Railway!

---

## 🚀 Part 2: Deploy to Railway

### Step 1: Create GitHub Repository

#### Option A: Using GitHub Desktop (Easiest)

1. **Download GitHub Desktop:** https://desktop.github.com/
2. **Install and sign in** with your GitHub account
3. **Click "Add" → "Add Existing Repository"**
4. **Browse to:** `K:\p4\halloween_contest`
5. **Click "Publish Repository"**
   - Name: `halloween-contest`
   - Description: Halloween Costume Contest App
   - ☐ Keep this code private (uncheck for public)
6. **Click "Publish repository"**

Done! Your code is on GitHub!

#### Option B: Using Command Line

```bash
cd K:\p4\halloween_contest

# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Halloween costume contest with multiple photos and backups"

# Create repository on github.com first, then:
git remote add origin https://github.com/YOUR_USERNAME/halloween-contest.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway

1. **Go to Railway:** https://railway.app

2. **Sign Up/Sign In:**
   - Click "Login"
   - Choose "Login with GitHub"
   - Authorize Railway

3. **Create New Project:**
   - Click "New Project"
   - Click "Deploy from GitHub repo"
   - Select **"halloween-contest"** (or your repo name)

4. **Wait for Deployment:**
   - Railway auto-detects Python/Flask
   - Builds and deploys automatically
   - Takes 2-3 minutes
   - Watch the logs in the deployment tab

5. **Generate Domain:**
   - Once deployed, click "Settings"
   - Scroll to "Domains"
   - Click "Generate Domain"
   - You'll get: `halloween-contest-production-xxxx.up.railway.app`

6. **Test Your Live Site:**
   - Click the domain link
   - App should load!
   - Test all features again

---

## 🎉 Your App is Live!

Your contest is now accessible from anywhere at:
```
https://halloween-contest-production-xxxx.up.railway.app
```

---

## 📱 Step 3: Generate QR Code with Your Railway URL

1. **Edit `generate_qr.py`:**

```python
# Find this line (around line 25):
url = f"http://{local_ip}:5000"

# Replace with your Railway URL:
url = "https://halloween-contest-production-xxxx.up.railway.app"
```

2. **Generate QR code:**

```bash
python generate_qr.py
```

3. **Print or display the QR code:**
   - File saved as: `contest_qr_code.png`
   - Print it out
   - Or display on a screen
   - Guests scan and access!

---

## 🔄 Updating Your Deployed App

Made changes and want to update the live site?

### Using GitHub Desktop:

1. Make your changes locally
2. Open GitHub Desktop
3. It shows changed files
4. Add commit message: "Updated feature X"
5. Click "Commit to main"
6. Click "Push origin"
7. Railway auto-deploys in 2-3 minutes!

### Using Command Line:

```bash
# After making changes:
git add .
git commit -m "Updated features"
git push

# Railway automatically redeploys!
```

---

## 📊 Monitoring Your Deployment

### Railway Dashboard

Access at: https://railway.app/dashboard

**What you can see:**
- **Deployments:** Build history and logs
- **Metrics:** CPU, memory, network usage
- **Logs:** Real-time application logs
- **Usage:** How much of your $5 credit used

### Check Logs:

1. Go to Railway dashboard
2. Click your project
3. Click "View Logs"
4. See real-time activity

**Useful for debugging:**
- Entry submissions
- Photo uploads
- Errors
- API calls

---

## 💾 Important: Backup Before Re-deploying

⚠️ **Warning:** On Railway free tier, uploaded files may be lost on re-deployment.

**Before pushing updates:**

1. Go to your admin page:
   ```
   https://your-app.up.railway.app/admin
   ```

2. Click "Download JSON Backup"

3. Save the file locally

4. Now you can safely re-deploy

5. After re-deploy, entries will be empty but you have the backup!

---

## 🎃 During Your Halloween Party

### Pre-Party Checklist:

- [ ] App deployed to Railway
- [ ] Test all features on live URL
- [ ] QR code generated with Railway URL
- [ ] QR code printed or ready to display
- [ ] Test QR code scan from phone
- [ ] Bookmark admin page for monitoring

### During Party:

1. **Display QR code** where guests can see it
2. **Tell guests:**
   - "Scan QR code to enter the contest"
   - "Upload your costume photos"
   - "Vote for your favorites"
3. **Monitor admin dashboard:**
   - Watch entries come in
   - Check statistics
   - Download backup periodically (just in case!)

### Post-Party:

1. **Download final backup:**
   - Go to `/admin`
   - Click "Download JSON Backup"
   - Click "Export to CSV"
   - Save both files

2. **Optional: Stop the app:**
   - If one-time event, can delete from Railway
   - Your local backup has all data
   - Photos are in your local `uploads/` folder

---

## 🐛 Troubleshooting

### Issue: "Build Failed" on Railway

**Check:**
- `requirements.txt` exists
- All dependencies listed
- `Procfile` exists with: `web: gunicorn app:app`

**Solution:**
```bash
# Verify files exist:
cat requirements.txt
cat Procfile

# If Procfile missing, create it:
echo "web: gunicorn app:app" > Procfile
git add Procfile
git commit -m "Add Procfile"
git push
```

### Issue: "Application Error" after deploy

**Check Railway logs:**
1. Go to Railway dashboard
2. View logs
3. Look for error messages

**Common fixes:**
- Ensure `gunicorn` in requirements.txt
- Check `app.py` has no syntax errors
- Verify environment variables if any

### Issue: Photos not uploading

**Check:**
- File size < 16MB
- File is image format (jpg, png, gif, webp)
- Browser console for errors (F12)

### Issue: Carousel not working

**Check:**
- JavaScript enabled in browser
- No console errors
- Entry has `photos` array in data

### Issue: Running out of Railway credit

**Monitor usage:**
- Go to Railway dashboard
- Check "Usage" section
- Free tier: $5 credit/month
- Typical party uses: $0.10 - $0.50

**If running out:**
- Event should be fine (one evening)
- For longer: upgrade to paid tier ($5/month)

---

## 📈 Success Metrics

After your party, check:

### Admin Dashboard Stats:
- Total Entries
- Total Votes
- Total Photos
- Most voted costume

### CSV Analysis:
- Export to CSV
- Open in Excel
- Sort by votes
- Create charts
- Identify winner!

---

## 🎊 You're All Set!

### What You Have:

✅ **Tested locally** - All features working
✅ **Deployed to Railway** - Accessible globally
✅ **QR code ready** - Easy guest access
✅ **Multiple photos** - Better costume showcase
✅ **Automatic backups** - Data is safe
✅ **Admin dashboard** - Real-time monitoring

### Your URLs:

- **Live App:** `https://your-app.up.railway.app`
- **Admin:** `https://your-app.up.railway.app/admin`
- **Railway Dashboard:** `https://railway.app/dashboard`

### Next Steps:

1. Share your URL or QR code with guests
2. Let the contest begin!
3. Monitor from admin dashboard
4. Download results after party
5. Announce winner!

---

## 🆘 Need Help?

### Quick Checks:

```bash
# Test locally:
python app.py
# Then open: http://localhost:5000

# Check git status:
git status

# View Railway logs:
# Go to railway.app/dashboard → Your project → View Logs

# Re-generate requirements:
pip freeze > requirements.txt
```

### Support Resources:

- **Railway Docs:** https://docs.railway.app
- **Flask Docs:** https://flask.palletsprojects.com
- **GitHub Help:** https://docs.github.com

---

**Have a spooktacular Halloween party!** 🎃👻🦇

**Questions? Check:**
- `NEW_FEATURES.md` - Feature documentation
- `DEPLOY_CLOUD.md` - Detailed deployment guide
- `README.md` - General documentation

