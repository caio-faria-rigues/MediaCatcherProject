from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup
from re import sub

def requestSourceInfo(url):
    opts = {}
    with YoutubeDL(opts) as ydl: 
        info_dict = ydl.extract_info(url, download=False)
        duration = info_dict.get("duration", None)
        video_title = info_dict.get('title', None)
        thumb = info_dict.get("thumbnail", None)
        return video_title, duration, thumb
    

def audioDownloader(url, name, ext, thumb, ring):
    def progress(status):
        if status['status'] == 'downloading':
            percentage = float(status['_percent_str'][7:12]) / 100.0
            ring.visible = True if percentage < 1.0 else False
            ring.value = percentage
            ring.update()

    ydl_opts = {
    'format': f'bestaudio[ext={ext}]',
    'outtmpl': f'{name}.%(ext)s',
    'writethumbnail': thumb,
    'ffmpeg_location': r'C:\Users\Cliente\Vs_projects\Python\Media Saver\test\ffmpeg.exe',
    'embedthumbnail': thumb,
    'progress_hooks': [progress],
    'postprocessors': [{
        'key': 'FFmpegMetadata',
        'add_metadata': True,
    },
    {
        'key': 'FFmpegExtractAudio',
        'preferredcodec': f'{ext}',
        'preferredquality' : 'best',
    },
    {
        'key': 'EmbedThumbnail',
    },
    ]
    }

    with YoutubeDL(ydl_opts) as ydl:
        error = ydl.download(url)
        #add error popup

def videoDownloader(url, name, ext, res, ring):

    def progress(status):
        if status['status'] == 'downloading':
            percentage = float(status['_percent_str'][7:12]) / 100.0
            ring.visible = True if percentage < 1.0 else False
            ring.value = percentage
            ring.update()

    ydl_opts = {
    'format': f'bestvideo[ext={ext}][height<={res}]+bestaudio[ext={ext}]/best[ext={ext}]',
    'outtmpl': f'{name}.%(ext)s',
    'ffmpeg_location': r'C:\Users\Cliente\Vs_projects\Python\Media Saver\test\ffmpeg.exe',
    'progress_hooks': [progress]
    }

    with YoutubeDL(ydl_opts) as ydl:
        error = ydl.download(url)