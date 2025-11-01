# Railway Persistent Storage Setup

## 🚨 Problem
Railway uses **ephemeral storage** by default, meaning:
- Files persist between **restarts**
- Files are **LOST** when the service is **redeployed** or **rebuilt**
- Container rebuilds happen during: code updates, configuration changes, Railway platform updates

## ✅ Solution: Railway Volumes
Railway Volumes provide persistent storage that survives rebuilds and redeployments.

---

## 📋 Setup Instructions

### Step 1: Create a Railway Volume

1. **Go to your Railway project dashboard**
   - Visit: https://railway.app/dashboard
   - Click on your Halloween Contest project

2. **Navigate to the Volumes tab**
   - In your service (web service), click on the **"Variables"** tab
   - Look for **"Volume"** section or **"Add Volume"** button

3. **Create a new volume**
   - Click **"+ New Volume"**
   - **Volume Name**: `contest_data`
   - **Mount Path**: `/data`
   - **Size**: 1GB (sufficient for ~1000 photos)
   - Click **"Add"**

### Step 2: Set Environment Variable

1. **Still in your Railway service settings**
2. **Go to "Variables" tab**
3. **Click "+ New Variable"**
4. Add:
   ```
   Variable Name: DATA_DIR
   Value: /data
   ```
5. **Click "Add"**

### Step 3: Deploy the Updated Code

```bash
# Make sure you're in the project directory
cd K:\p4\halloween_contest

# Add all changes
git add .

# Commit
git commit -m "Add persistent storage support with Railway volumes"

# Push to Railway (this will trigger automatic deployment)
git push origin main
```

### Step 4: Verify Everything Works

1. **Check deployment logs** in Railway dashboard
2. Look for these log messages:
   ```
   📁 Data directory: /data
   📁 Upload folder: /data/uploads
   📁 Data file: /data/contest_data.json
   📁 Backup directory: /data/backups
   ```

3. **Test the application**:
   - Submit a test entry with a photo
   - Go to Admin page and verify the entry exists
   - **Trigger a redeploy** (change any variable and save)
   - After redeployment, **verify the entry still exists**

---

## 🎯 How It Works

### Before (Ephemeral Storage)
```
/app
├── uploads/           ❌ Lost on rebuild
├── contest_data.json  ❌ Lost on rebuild
└── backups/           ❌ Lost on rebuild
```

### After (Persistent Storage)
```
/app
└── (application code only)

/data (PERSISTENT VOLUME)
├── uploads/           ✅ Survives rebuilds
├── contest_data.json  ✅ Survives rebuilds
└── backups/           ✅ Survives rebuilds
```

---

## 🔄 What Changed in the Code

The app now uses environment variables to determine storage location:

```python
# Old (ephemeral)
UPLOAD_FOLDER = 'uploads'
DATA_FILE = 'contest_data.json'

# New (persistent)
DATA_DIR = os.environ.get('DATA_DIR', os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(DATA_DIR, 'uploads')
DATA_FILE = os.path.join(DATA_DIR, 'contest_data.json')
BACKUP_DIR = os.path.join(DATA_DIR, 'backups')
```

**Local Development**: When `DATA_DIR` is not set, it defaults to the project directory
**Railway Production**: When `DATA_DIR=/data`, all data goes to the persistent volume

---

## 💰 Railway Volume Pricing

- **Free Tier**: Includes 1GB volume storage (perfect for your use case)
- **Storage costs**: $0.25/GB/month beyond free tier
- **For 30 people with 5 photos each** (~150 photos):
  - Average photo size: 2-3 MB
  - Total storage needed: ~450 MB
  - **Fits easily in the free tier!**

---

## 🧪 Testing Persistence

### Test 1: Restart Test
```bash
# In Railway dashboard, click "Restart" button
# Your data should persist ✅
```

### Test 2: Redeploy Test
```bash
# Make any code change and git push
git commit --allow-empty -m "Test persistence"
git push origin main
# Your data should persist ✅
```

### Test 3: Manual Volume Check
In Railway dashboard:
1. Click on your service
2. Go to "Settings" → "Deploy Logs"
3. Look for the log messages showing `/data` paths
4. All entries and photos should still be there

---

## 🔧 Troubleshooting

### Volume Not Created
**Symptom**: Logs show `📁 Data directory: /app` instead of `/data`

**Solution**:
1. Verify the volume is created in Railway dashboard
2. Verify the `DATA_DIR` environment variable is set to `/data`
3. Redeploy the service

### Permission Errors
**Symptom**: `PermissionError: [Errno 13] Permission denied: '/data/uploads'`

**Solution**:
- Railway volumes are mounted with correct permissions automatically
- If you see this error, try deleting and recreating the volume

### Data Still Lost After Setup
**Symptom**: Data disappears even with volume configured

**Solution**:
1. Check Railway logs: `Railway CLI` → `railway logs`
2. Verify `DATA_DIR=/data` is set in environment variables
3. Verify volume mount path is `/data`
4. Make sure you're not manually deleting data via the Reset button

---

## 🎉 Benefits of This Setup

✅ **Survives redeployments** - Your contest data is safe during updates
✅ **Automatic backups** - Still creates timestamped JSON backups
✅ **No code changes needed** - Works locally without Railway volumes
✅ **Free** - Fits within Railway's free tier limits
✅ **Scalable** - Easy to upgrade volume size if needed

---

## 📞 Need Help?

If data is still being lost:
1. Check Railway logs for error messages
2. Verify volume is mounted: Look for "📁 Data directory: /data" in logs
3. Test with a small entry to confirm persistence
4. Contact Railway support if issues persist

---

## 🔐 Backup Strategy

Even with persistent volumes, it's good to have backups:

1. **Automatic backups** (already implemented):
   - Creates timestamped backups after each change
   - Keeps last 10 backups
   - Stored in `/data/backups/`

2. **Manual backups**:
   - Go to `/admin` page
   - Click "Download Data (JSON)" - saves all data
   - Click "Export as CSV" - saves entries in spreadsheet format
   - Keep these files on your local computer

3. **Railway Volume Snapshots** (future):
   - Railway is working on volume snapshot features
   - Check their dashboard for updates

---

## 🚀 Ready to Deploy!

Follow the steps above, and your data will persist through all deployments! 🎃

