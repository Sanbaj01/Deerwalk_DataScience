from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print('Title : ', yt.title)
print('View : ', yt.views)

yd = yt.streams.get_by_resolution('480p')

yd.downlaod("\videos")

