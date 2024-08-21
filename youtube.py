import yt_dlp
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Your API key
API_KEY = os.getenv('YOUTUBE_API_KEY')

def search_youtube(query):
    search_url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'key': API_KEY,
        'type': 'video',
        'maxResults': 1
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    
    if 'items' in data and len(data['items']) > 0:
        video = data['items'][0]
        video_id = video['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        return None


# Function to download audio from YouTube
def download_audio(url, filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
