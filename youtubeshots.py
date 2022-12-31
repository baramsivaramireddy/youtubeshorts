from moviepy.editor import *
from PIL import Image
import requests
import json
import os

# resource link https://github.com/D3vd/Meme_Api


# these number of memes are enough for creating a short in youtube
NoOfMemes = 5
subreddit= "memes"
url = f'https://meme-api.com/gimme/{subreddit}/{NoOfMemes}'

#calling api 
response = requests.get(url)
data = response.json()


# getting images from internet and writing it to disk

for i in range(NoOfMemes):

    imgRaw = requests.get(data["memes"][i]['url'])
    with open(f'{str(i)}.jpg',"wb") as f :
        f.write(imgRaw.content)


# creating appropriate meme with perfect ascept ratio.

for i in range(NoOfMemes):
    backgroundImage = Image.new(mode='RGB',size=(1080,1920))
    memeImg = Image.open(f'{str(i)}.jpg').resize((1000,1840))
    backgroundImage.paste(memeImg,box=(50,50))
    backgroundImage.save(f'{str(i)}.jpg')

# creating video from images with audio and saving it 

clips = []


for i in range(NoOfMemes):
    clip = ImageClip(f'{str(i)}.jpg').set_audio(AudioFileClip(r'audio.mp3').subclip(0,)).set_duration(15)
    clips.append(clip)

final = concatenate_videoclips(clips)



# reading initial dat like how many videos we created so far 
with open('./basicInfo.json',) as f :
    Noofvideos= json.load(f)['NoOfVideos']

currentVideoSerialNumber = Noofvideos+1
# create a new folder for video data 
os.mkdir(f"./database/{str(currentVideoSerialNumber)}")

#writing the video and json data for future reference
final.write_videofile(rf'./database/{currentVideoSerialNumber}/funny_memes.mp4.mp4',fps=1)
with open(f"./database/{str(currentVideoSerialNumber)}/Resopnse.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)



# updating the basicinfo for creating new video
with open('./basicInfo.json', 'w', encoding='utf-8') as f:
    json.dump({"NoOfVideos": currentVideoSerialNumber}, f,indent=4)


#removing the images

for i in range(NoOfMemes):

   os.remove(f'{str(i)}.jpg')
