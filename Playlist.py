from pytube import Playlist
py = Playlist("https://www.youtube.com/playlist?list=PLtgiThe4j67rAoPmnCQmcgLS4iIc5ungg")
print(f'Downloading: {py.title}')
for videos in py.videos:
      videos.streams.first().download()