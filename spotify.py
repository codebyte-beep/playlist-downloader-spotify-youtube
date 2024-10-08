import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()


# Spotify API credentials
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# Initialize SpotifyOAuth
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope="playlist-read-private playlist-read-collaborative")

sp = spotipy.Spotify(auth_manager=sp_oauth)

# Function to fetch user's playlists
def get_user_playlists():
    results = sp.current_user_playlists()
    playlists = results['items']
    return playlists

# Function to search for public playlists
def search_public_playlists(query):
    results = sp.search(q=query, type='playlist', limit=1)
    playlists = results['playlists']['items']
    return playlists

# Function to find playlist ID by name from user's playlists
def find_user_playlist_id(playlist_name):
    playlists = get_user_playlists()
    for playlist in playlists:
        if playlist['name'].lower() == playlist_name.lower():
            return playlist['id']
    return None

# Function to find playlist ID by name from public playlists
def find_public_playlist_id(playlist_name):
    playlists = search_public_playlists(playlist_name)
    for playlist in playlists:
        if playlist['name'].lower() == playlist_name.lower():
            return playlist['id']
    return None

# Function to fetch tracks from a playlist
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    return tracks

