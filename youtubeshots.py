# fetch meme from provider .

import os 
import json
import requests
# resource link https://github.com/D3vd/Meme_Api


# these number of memes are enough for creating a short in youtube
NoOfMemes = 10
subreddit = 'memes'
url = f'https://meme-api.com/gimme/{subreddit}/{NoOfMemes}'

#calling api 


response = requests.get(url)
data = response.json()

# reading initial dat like how many videos we created so far 
with open('./basicdata.json',) as f :
    initialData = json.load(f)


# creaating an empty directory for video making
os.mkdir(str(initialData["NoOfVideos"]))

with open('./basicdata.json', 'w', encoding='utf-8') as f:
    json.dump({"NoOfVideos":initialData["NoOfVideos"]+1}, f, ensure_ascii=False, indent=4)


#recording the complete data for video

with open(f'{str(initialData["NoOfVideos"])}/info.json', 'w', encoding='utf-8') as infoFile:
    json.dump(data, infoFile, ensure_ascii=False, indent=4)



# write images to a directory .

for i in range(NoOfMemes):
    r = requests.get(data['memes'][i]['url'])
    with open(str(initialData["NoOfVideos"])+'/'+str(i)+'.jpg', "wb") as f:
        f.write(r.content)


