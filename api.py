import requests
import datetime as dt
from tools import *

h = "https://hilbert.himkwtn.me/checkin"

def gather_info(cr,resv_info):
    cr.read_card()
    #nw = dt.datetime.now()
    #nw = nw.strftime("%Y-%m-%d")
    nw = "2020-04-04"
    host = h
    params = {"nationalID":cr.card_data["nationalID"],"date":nw}
    ret = requests.get(host,params)
    if ret.status_code == 200:
        temp = dict(ret.json())
        for i in temp:
            resv_info[i] = temp[i]
        #print (resv_info)    
        load_pic(temp['rooms'][0]['photos'][0]['photo_url'])
        resize_pic("room_image.jpg",350,"resized_room")
        resize_pic("room_image.jpg",250,"resized_room2")

def request_OTP(resv_info,refn):
    host = (h+"/generate-otp/{}").format(resv_info["id"])
    ret = requests.post(host)
    print(ret.request.headers)
    if ret.status_code == 200:
        temp = dict(ret.json())
        for i in temp:
            refn[i] = temp[i]
    
    print(ret)
    
def verify_OTP(resv_info,otp,token):
    host = h+"/verify-otp/{}".format(resv_info["id"])
    notp = ""
    for i in otp:
        notp += str(i)    
    body = {'otp':notp}
    ret = requests.post(host,json = body)
    if ret.status_code == 200:
        temp = dict(ret.json())
        for i in temp:
            token[i] = temp[i]
    print(token)

def send_data(cr,token):
    print(cr.card_data)
    host = h
    hdr = {'Authentication':'Bearer '+token['token']}
    ret = requests.post(host,files = cr.card_data,headers=hdr)
    print(ret)
