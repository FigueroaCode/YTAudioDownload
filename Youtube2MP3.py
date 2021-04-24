'''
Requirements:
(Windows)
- Use powershell as administrator
- Run: Set-ExecutionPolicy Unrestricted
- Install Chocolatey: Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
- Restart shell and do first 2 steps again
- Run: .\env\scripts\activate
- Run: pip install youtube-dl
- Run: choco install ffmpeg

How to use:
- Run while in virtual enviornment in powershell in :
    python .\Youtube2MP3.py name_of_file.txt
- Text file should have the links line by line (there is an example file: example_links.txt for reference)
'''

import youtube_dl
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        'outtmpl': './audio_files/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        links_file = open(filename, 'r')
        links = links_file.read().splitlines()
        ydl.download(links)
