from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import secrets

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['SECRET_KEY'] = secrets.token_hex(16)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
DATA_FILE = 'contest_data.json'

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_data():
    """Load contest data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'entries': [],
        'votes': {},
        'settings': {
            'show_votes': False,
            'voting_enabled': True
        }
    }

def save_data(data):
    """Save contest data to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def backup_data():
    """Create a backup of contest data"""
    if not os.path.exists(DATA_FILE):
        return
    
    # Create backups directory
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)
    
    # Create timestamped backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(backup_dir, f'contest_backup_{timestamp}.json')
    
    # Copy current data to backup
    data = load_data()
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Keep only last 10 backups
    backups = sorted([f for f in os.listdir(backup_dir) if f.startswith('contest_backup_')])
    if len(backups) > 10:
        for old_backup in backups[:-10]:
            os.remove(os.path.join(backup_dir, old_backup))

@app.route('/')
def index():
    """Main page - shows participate and vote options"""
    return render_template('index.html')

@app.route('/participate')
def participate():
    """Page for submitting entries"""
    return render_template('participate.html')

@app.route('/vote')
def vote():
    """Page for voting on entries"""
    return render_template('vote.html')

@app.route('/results')
def results():
    """Page showing contest results"""
    return render_template('results.html')

@app.route('/api/entries', methods=['GET'])
def get_entries():
    """Get all contest entries"""
    data = load_data()
    entries = data['entries']
    
    # Calculate vote counts
    for entry in entries:
        entry_id = entry['id']
        entry['vote_count'] = len(data['votes'].get(entry_id, []))
    
    return jsonify({
        'entries': entries,
        'settings': data['settings']
    })

@app.route('/api/submit', methods=['POST'])
def submit_entry():
    """Submit a new contest entry"""
    try:
        data = load_data()
        
        # Get form data
        name = request.form.get('name', '').strip()
        costume_name = request.form.get('costume_name', '').strip()
        description = request.form.get('description', '').strip()
        
        if not name or not costume_name:
            return jsonify({'error': 'Name and costume name are required'}), 400
        
        # Handle multiple file uploads
        if 'photos' not in request.files:
            return jsonify({'error': 'At least one photo is required'}), 400
        
        files = request.files.getlist('photos')
        if not files or all(f.filename == '' for f in files):
            return jsonify({'error': 'No files selected'}), 400
        
        # Save all valid photos
        saved_filenames = []
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        for idx, file in enumerate(files):
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Add timestamp and index to avoid conflicts
                filename = f"{timestamp}_{idx}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                saved_filenames.append(filename)
        
        if not saved_filenames:
            return jsonify({'error': 'No valid images uploaded. Please upload image files.'}), 400
        
        # Create new entry
        entry_id = str(len(data['entries']) + 1)
        new_entry = {
            'id': entry_id,
            'name': name,
            'costume_name': costume_name,
            'description': description,
            'photos': saved_filenames,  # Multiple photos now
            'timestamp': datetime.now().isoformat()
        }
        
        data['entries'].append(new_entry)
        save_data(data)
        
        # Create automatic backup
        backup_data()
        
        return jsonify({'success': True, 'entry': new_entry})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/vote', methods=['POST'])
def submit_vote():
    """Submit a vote for an entry"""
    try:
        vote_data = request.json
        entry_id = vote_data.get('entry_id')
        voter_id = vote_data.get('voter_id')  # Could be session ID or name
        
        if not entry_id or not voter_id:
            return jsonify({'error': 'Entry ID and voter ID required'}), 400
        
        data = load_data()
        
        if not data['settings']['voting_enabled']:
            return jsonify({'error': 'Voting is currently disabled'}), 403
        
        # Check if voter has already voted
        for eid, voters in data['votes'].items():
            if voter_id in voters:
                # Remove previous vote
                data['votes'][eid].remove(voter_id)
        
        # Add new vote
        if entry_id not in data['votes']:
            data['votes'][entry_id] = []
        
        if voter_id not in data['votes'][entry_id]:
            data['votes'][entry_id].append(voter_id)
        
        save_data(data)
        
        return jsonify({'success': True})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/settings', methods=['POST'])
def update_settings():
    """Update contest settings (admin only)"""
    try:
        settings_data = request.json
        data = load_data()
        
        if 'show_votes' in settings_data:
            data['settings']['show_votes'] = settings_data['show_votes']
        
        if 'voting_enabled' in settings_data:
            data['settings']['voting_enabled'] = settings_data['voting_enabled']
        
        save_data(data)
        
        return jsonify({'success': True, 'settings': data['settings']})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        # Return a placeholder image if file not found
        return "File not found", 404

@app.route('/api/backup/download')
def download_backup():
    """Download current contest data as JSON"""
    try:
        data = load_data()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        response = jsonify(data)
        response.headers['Content-Disposition'] = f'attachment; filename=contest_data_{timestamp}.json'
        response.headers['Content-Type'] = 'application/json'
        
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/backup/export-csv')
def export_csv():
    """Export contest data as CSV"""
    try:
        import csv
        from io import StringIO
        
        data = load_data()
        output = StringIO()
        
        # Write entries
        writer = csv.writer(output)
        writer.writerow(['ID', 'Name', 'Costume Name', 'Description', 'Photo Count', 'Votes', 'Timestamp'])
        
        for entry in data['entries']:
            vote_count = len(data['votes'].get(entry['id'], []))
            photo_count = len(entry.get('photos', [entry.get('photo', '')]))
            writer.writerow([
                entry['id'],
                entry['name'],
                entry['costume_name'],
                entry.get('description', ''),
                photo_count,
                vote_count,
                entry['timestamp']
            ])
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output.seek(0)
        
        from flask import Response
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': f'attachment; filename=contest_results_{timestamp}.csv'}
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/admin')
def admin():
    """Admin page for backup and data management"""
    return render_template('admin.html')

if __name__ == '__main__':
    # Check if running in production or development
    import sys
    is_production = os.environ.get('RENDER') or os.environ.get('RAILWAY_ENVIRONMENT')
    
    if not is_production:
        print("\n" + "="*60)
        print("🎃 HALLOWEEN COSTUME CONTEST APP 🎃")
        print("="*60)
        print("\nStarting server...")
        print("\nAccess the app at:")
        print("  → http://localhost:5000")
        print("  → Or your local IP for other devices on the network")
        print("\nTo find your local IP:")
        print("  → Windows: Run 'ipconfig' and look for IPv4 Address")
        print("  → Mac/Linux: Run 'ifconfig' or 'ip addr'")
        print("\nPress Ctrl+C to stop the server")
        print("="*60 + "\n")
    
    # Get port from environment variable (for cloud deployment) or use 5000
    port = int(os.environ.get('PORT', 5000))
    debug = not is_production
    
    app.run(host='0.0.0.0', port=port, debug=debug)


