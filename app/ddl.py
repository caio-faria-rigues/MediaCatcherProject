from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup

def requestSourceInfo(url):
    opts = {}
    with YoutubeDL(opts) as ydl: 
        info_dict = ydl.extract_info(url, download=False)
        duration = info_dict.get("duration", None)
        video_title = info_dict.get('title', None)
        thumb = info_dict.get("thumbnail", None)
        return video_title, duration, thumb