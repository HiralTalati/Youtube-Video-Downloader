from pytube import YouTube
link = "https://www.youtube.com/watch?v=EAYlckSaviI"
youtube1 = YouTube(link)
#print(youtube1.title)
#print(youtube1.thumbnail_url)
#videos = youtube1.streams.all()
videos1 = youtube1.streams.filter(only_audio = True)
stream_list = list(enumerate(videos1))
for i in stream_list:
    print(i)
print()
stream_option = int(input("Enter any streaming_options: "))
videos1[stream_option].download()
print("Your audio is successfully Downloaded!")