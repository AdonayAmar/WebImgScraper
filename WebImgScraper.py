from PIL import Image
from warnings import catch_warnings
from bs4 import BeautifulSoup
import requests

url = 'https://www.reddit.com/'
urlhtml = requests.get(url).text

soup = BeautifulSoup(urlhtml, 'lxml')
image = soup.find_all('img')
count = 0
for images in image:
    try:
        src = images['src']
        if src.split("http",0):
            imgurl = src
        else:
            imgurl = f"{url}{src}"
        print(imgurl)
        img = Image.open(requests.get(imgurl, stream = True).raw)
        if src.split(".png",-1):
            img.save(f'Images\image{count}.png')
        if src.split(".jpeg",-1):
            img.save(f'Images\image{count}.jpeg')
    except:
        pass
    count+=1