import qrcode
import socket

def get_local_ip():
    """Get the local IP address of this machine"""
    try:
        # Create a socket to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't actually connect, just determines routing
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "localhost"

def generate_qr_code():
    """Generate a QR code for the contest URL"""
    local_ip = get_local_ip()
    # url = f"http://{local_ip}:5000"
    url = f"https://halloweencontest-production.up.railway.app/"
    
    print("\n" + "="*60)
    print("🎃 HALLOWEEN COSTUME CONTEST - QR CODE GENERATOR 🎃")
    print("="*60)
    print(f"\nYour local IP address: {local_ip}")
    print(f"Contest URL: {url}")
    print("\nGenerating QR code...")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    filename = "contest_qr_code.png"
    img.save(filename)
    
    print(f"\n✅ QR code saved as: {filename}")
    print("\nInstructions:")
    print("  1. Make sure the Flask app is running (python app.py)")
    print("  2. Print or display this QR code at your party")
    print("  3. Guests can scan it with their phones to access the contest")
    print("\nNote: Your computer and guests' phones must be on the same WiFi network!")
    print("="*60 + "\n")

if __name__ == "__main__":
    generate_qr_code()


