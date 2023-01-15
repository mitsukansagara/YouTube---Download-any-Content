from pytube import YouTube
link = input("Enter link of your video here: ")
content = YouTube(link)
stream = content.streams.get_highest_resolution()
path = input("Enter your path to save content: ")
stream.download(path)
print("Hurray! Your content is in place.")

#any given content cannot have a duplicate in the same folder