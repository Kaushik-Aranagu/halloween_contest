#!/usr/bin/env python3
"""
Test script to verify persistent storage configuration
Run this locally to ensure everything is configured correctly
"""

import os
import json

def test_persistence():
    """Test that the app correctly uses DATA_DIR"""
    
    print("=" * 60)
    print("🧪 TESTING PERSISTENT STORAGE CONFIGURATION")
    print("=" * 60)
    
    # Test 1: Check environment variable
    print("\n✓ Test 1: Environment Variable")
    data_dir = os.environ.get('DATA_DIR', os.path.dirname(os.path.abspath(__file__)))
    print(f"   DATA_DIR: {data_dir}")
    
    if data_dir == os.path.dirname(os.path.abspath(__file__)):
        print("   ℹ️  Using local directory (expected for local dev)")
    else:
        print(f"   ℹ️  Using custom directory: {data_dir}")
    
    # Test 2: Construct paths
    print("\n✓ Test 2: Path Construction")
    upload_folder = os.path.join(data_dir, 'uploads')
    data_file = os.path.join(data_dir, 'contest_data.json')
    backup_dir = os.path.join(data_dir, 'backups')
    
    print(f"   Upload folder: {upload_folder}")
    print(f"   Data file: {data_file}")
    print(f"   Backup directory: {backup_dir}")
    
    # Test 3: Check if directories exist
    print("\n✓ Test 3: Directory Existence")
    for name, path in [
        ("Upload folder", upload_folder),
        ("Backup directory", backup_dir)
    ]:
        if os.path.exists(path):
            print(f"   ✅ {name} exists: {path}")
        else:
            print(f"   ⚠️  {name} doesn't exist (will be created on app start): {path}")
    
    # Test 4: Check data file
    print("\n✓ Test 4: Data File")
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
        entry_count = len(data.get('entries', []))
        vote_count = len(data.get('votes', {}))
        print(f"   ✅ Data file exists")
        print(f"   📊 Entries: {entry_count}")
        print(f"   🗳️  Votes: {vote_count}")
    else:
        print(f"   ℹ️  Data file doesn't exist yet (will be created on first entry)")
    
    # Test 5: Railway environment check
    print("\n✓ Test 5: Railway Environment")
    is_railway = os.environ.get('RAILWAY_ENVIRONMENT')
    if is_railway:
        print(f"   🚂 Running on Railway: {is_railway}")
        if os.environ.get('DATA_DIR') == '/data':
            print("   ✅ DATA_DIR correctly set to /data")
        else:
            print("   ❌ WARNING: DATA_DIR should be set to /data in Railway!")
    else:
        print("   💻 Running locally (not Railway)")
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    
    if is_railway and os.environ.get('DATA_DIR') != '/data':
        print("❌ ISSUE DETECTED:")
        print("   Set DATA_DIR=/data in Railway environment variables!")
    elif is_railway:
        print("✅ Configuration looks good for Railway deployment!")
        print("   Make sure you've created a volume mounted at /data")
    else:
        print("✅ Configuration looks good for local development!")
        print("   Deploy to Railway and set DATA_DIR=/data for production")
    
    print("\n📖 For setup instructions, see: QUICK_SETUP_PERSISTENCE.txt")
    print("=" * 60)

if __name__ == '__main__':
    test_persistence()

