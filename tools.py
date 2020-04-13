import requests
import PIL
from time import sleep
from picamera import PiCamera
from PIL import Image

camera = PiCamera()

def load_pic(url):
    img_data = requests.get(url).content
    with open('room_image.jpg', 'wb') as handler:
        handler.write(img_data)

def resize_pic(pic,bw,name):
    basewidth = bw
    img = Image.open(pic)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('{}.jpg'.format(name))

def capture_pic(cr):
    camera.resolution = (640, 480)
    camera.start_preview(alpha=192)
    sleep(3)
    camera.capture("selfie.jpg")
    camera.stop_preview()
    resize_pic("selfie.jpg",280,"resized_selfie")
    with open("selfie.jpg", "rb") as img_file:
        x = img_file.read()
        cr.card_data['kioskPhoto'] = x