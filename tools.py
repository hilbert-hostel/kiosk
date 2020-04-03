import requests
import PIL
from PIL import Image

def load_pic(url):
    img_data = requests.get(url).content
    with open('room_image.jpg', 'wb') as handler:
        handler.write(img_data)

def resize_pic(pic,bw):
    basewidth = bw
    img = Image.open(pic)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('resized_image.jpg')