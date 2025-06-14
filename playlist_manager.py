import json
import pyperclip
import os

DB_FILE = 'playlist_db.json'

# Default playlists
DEFAULT_PLAYLISTS = {
    ('happy', 'clear'): ['Happy – Pharrell Williams', 'Walking on Sunshine – Katrina & The Waves'],
    ('sad', 'rain'): ['Someone Like You – Adele', 'Fix You – Coldplay'],
    ('chill', 'clouds'): ['Weightless – Marconi Union', 'Sunset Lover – Petit Biscuit'],
    ('energetic', 'clear'): ['Can’t Stop – Red Hot Chili Peppers', 'Don’t Stop Me Now – Queen'],
    ('sad', 'snow'): ['Skinny Love – Bon Iver', 'The Night We Met – Lord Huron'],
}

def load_playlists():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    else:
        return DEFAULT_PLAYLISTS.copy()

def save_playlists(playlists):
    with open(DB_FILE, 'w') as f:
        json.dump(playlists, f, indent=4)

def get_playlist(mood, weather, playlists):
    return playlists.get((mood, weather), ['Shape of You – Ed Sheeran', 'Blinding Lights – The Weeknd'])

def export_playlist(playlist, filename='playlist.txt'):
    with open(filename, 'w') as f:
        for song in playlist:
            f.write(song + '\n')

def copy_to_clipboard(playlist):
    pyperclip.copy('\n'.join(playlist))
