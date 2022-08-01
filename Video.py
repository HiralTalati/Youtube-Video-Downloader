from pytube import YouTube
link = "https://www.youtube.com/watch?v=EAYlckSaviI"
youtube1 = YouTube(link)
print(youtube1.title)   # for title of video
print(youtube1.thumbnail_url) #for thumbnail of video
videos = youtube1.streams.all()
stream_list = list(enumerate(videos))
for i in stream_list:
    print(i)
print()
stream_option = int(input("Enter any streaming_options: "))
videos[stream_option].download()
print("Your video is successfully Downloaded!")
