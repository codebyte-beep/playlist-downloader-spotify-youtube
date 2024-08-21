from spotify import get_playlist_tracks, find_user_playlist_id, find_public_playlist_id
from youtube import search_youtube, download_audio
import os

def main():
    # Create 'songs' directory if it does not exist
    if not os.path.exists('songs'):
        os.makedirs('songs')
    
    # Get playlist name from user input
    playlist_name = input("Enter the name of the playlist: ")
    
    # First, try to find the playlist in the user's playlists
    playlist_id = find_user_playlist_id(playlist_name)
    if not playlist_id:
        # If not found in user's playlists, search for public playlists
        playlist_id = find_public_playlist_id(playlist_name)
        if not playlist_id:
            print(f"Playlist '{playlist_name}' not found.")
            return
    
    # Fetch tracks from the specified playlist
    tracks = get_playlist_tracks(playlist_id)
    
    if not tracks:
        print("No tracks found. Exiting...")
        return
    
    # Download each track
    for item in tracks:
        track = item['track']
        query = f"{track['name']} {', '.join(artist['name'] for artist in track['artists'])}"
        print(f"Searching for {query} on YouTube...")
        youtube_url = search_youtube(query)
        print(youtube_url)
        if youtube_url:
            filename = os.path.join('songs', f"{track['name']}.mp3")
            print(f"Downloading {track['name']} from {youtube_url}")
            download_audio(youtube_url, filename)
            print(f"{track['name']} downloaded successfully.")
        else:
            print(f"Could not find {track['name']} on YouTube.")

if __name__ == "__main__":
    main()












