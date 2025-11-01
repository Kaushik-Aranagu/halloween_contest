"""
Setup checker for Halloween Costume Contest App
Run this to verify everything is configured correctly
"""

import sys
import os

def check_python_version():
    """Check if Python version is sufficient"""
    print("Checking Python version...", end=" ")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (Need 3.7+)")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\nChecking dependencies...")
    required = ['flask', 'qrcode', 'PIL']
    all_good = True
    
    for package in required:
        try:
            if package == 'PIL':
                import PIL
                print(f"  ✅ Pillow: {PIL.__version__}")
            else:
                module = __import__(package)
                version = getattr(module, '__version__', 'unknown')
                print(f"  ✅ {package}: {version}")
        except ImportError:
            print(f"  ❌ {package}: Not installed")
            all_good = False
    
    return all_good

def check_file_structure():
    """Check if all necessary files exist"""
    print("\nChecking file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'generate_qr.py',
        'templates/index.html',
        'templates/participate.html',
        'templates/vote.html',
        'templates/results.html'
    ]
    
    all_good = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - Missing!")
            all_good = False
    
    return all_good

def check_port():
    """Check if port 5000 is available"""
    print("\nChecking port availability...")
    import socket
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 5000))
        sock.close()
        
        if result == 0:
            print("  ⚠️  Port 5000 is in use (app might already be running)")
            print("     If the app isn't running, you may need to change the port")
            return True
        else:
            print("  ✅ Port 5000 is available")
            return True
    except:
        print("  ⚠️  Unable to check port")
        return True

def check_network():
    """Get and display network information"""
    print("\nChecking network configuration...")
    import socket
    
    try:
        # Get hostname
        hostname = socket.gethostname()
        print(f"  Computer name: {hostname}")
        
        # Get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        
        print(f"  ✅ Local IP address: {local_ip}")
        print(f"\n  Your contest URL will be: http://{local_ip}:5000")
        print(f"  (Use this URL in the QR code)")
        
        return True
    except:
        print("  ⚠️  Could not determine network configuration")
        print("     Make sure you're connected to WiFi")
        return False

def print_summary(results):
    """Print summary of checks"""
    print("\n" + "="*60)
    print("SETUP CHECK SUMMARY")
    print("="*60)
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n✅ All checks passed! You're ready to go!")
        print("\nNext steps:")
        print("  1. Run: python app.py")
        print("  2. Run: python generate_qr.py")
        print("  3. Access the app in your browser")
        print("\nSee QUICK_START.md for detailed instructions.")
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\nCommon fixes:")
        if not results['dependencies']:
            print("  • Install dependencies: pip install -r requirements.txt")
        if not results['python']:
            print("  • Update Python to version 3.7 or higher")
        if not results['files']:
            print("  • Make sure all files are downloaded/extracted correctly")
    
    print("="*60 + "\n")

def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("🎃 HALLOWEEN COSTUME CONTEST - SETUP CHECKER 🎃")
    print("="*60 + "\n")
    
    results = {
        'python': check_python_version(),
        'dependencies': check_dependencies(),
        'files': check_file_structure(),
        'port': check_port(),
        'network': check_network()
    }
    
    print_summary(results)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCheck cancelled by user.")
    except Exception as e:
        print(f"\n\n❌ Error during check: {e}")
        print("Please report this issue if the problem persists.")


