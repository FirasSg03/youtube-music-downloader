from yt_dlp import YoutubeDL

def download_playlist_as_mp3(playlist_url, output_path='./songs'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
        'noplaylist': False,  # Important! Allows playlist download
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == '__main__':
    playlist_url = input("Enter URL: ")
    download_playlist_as_mp3(playlist_url)
    print("Download complete!")
