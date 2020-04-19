import requests
import datetime as dt
from tools import *

h = "https://hilbert.himkwtn.me/checkIn"
h2 = "https://hilbert.himkwtn.me/checkOut"
h3 = "https://search-hilbert-huc7fjahm5ghi5gqmzhpfbhb6y.ap-southeast-1.es.amazonaws.com/hilbert/_doc"

def gather_info(cr,resv_info):
    cr.read_card()
    nw = dt.datetime.now()
    #nw = nw.isoformat()
    nw = nw.strftime("%Y-%m-%d")
    nw = "2020-04-17"
    host = h
    params = {"nationalID":cr.card_data["nationalID"],"date":nw}
    ret = requests.get(host,params)
    print("get_resv:")
    print(ret)
    if ret.status_code == 200:
        temp = dict(ret.json())
        for i in temp:
            resv_info[i] = temp[i]    
        load_pic(temp['rooms'][0]['photos'][0]['photo_url'])
        resize_pic("room_image.jpg",350,"resized_room")
        resize_pic("room_image.jpg",250,"resized_room2")
    elif ret.status_code == 500:
        print("Getting booking info failed with code status 500")
        # send_log("Getting booking info failed with code status 500")

def request_OTP(resv_info,refn):
    host = (h+"/generate-otp/{}").format(resv_info["id"])
    ret = requests.post(host)
    print(ret)
    if ret.status_code == 200:
        temp = dict(ret.json())
        for i in temp:
            refn[i] = temp[i]
    
    elif ret.status_code == 500:
        print("Requesting OTP failed with code status 500")
        # send_log("Requesting OTP failed with code status 500")
    
    
    
def verify_OTP(resv_info,otp,token):
    host = h+"/verify-otp/{}".format(resv_info["id"])
    notp = ""
    for i in otp:
        notp += str(i)    
    body = {'otp':notp}
    ret = requests.post(host,json = body)
    print(ret)
    
    if ret.status_code == 200:
        temp = dict(ret.json())
        for i in temp:
            token[i] = temp[i]
            return True
    
    elif ret.status_code == 400:
        print("User puts incorrect OTP")
        # send_log("User puts incorrect OTP")
    
    elif ret.status_code == 500:
        print("OTP verification failed with code status 500")
        # send_log("Verifying OTP failed with code status 500")
    
    return False
    
def send_data(cr,token):
    cdata = cr.card_data
    photo = {}
    photo["kioskPhoto"] = cr.card_data["kioskPhoto"]
    photo["idCardPhoto"] = cr.card_data["idCardPhoto"]
    cdata.pop("kioskPhoto")
    cdata.pop("idCardPhoto")
    host = h
    hdr = {'Authorization':'Bearer '+token['token']}
    print(photo.keys())
    print(cdata.keys())
    ret = requests.post(host,files=photo,data=cdata,headers=hdr)
    print(ret)
    
def check_out(resv_info):
    payload = {"reservationID":resv_info}
    host = h2
    ret = requests.post(host,json=payload)
    print(ret)
    if ret.status_code == 200:
        return True
    elif ret.status_code == 500:
        print("Check-out failed with code status 500")
        #send_log("Check-out failed with code status 500")
    return False

def send_log(message,level="error"):
    nw = dt.datetime.now()
    ts = int(dt.datetime.timestamp(nw))
    host = h3
    log = {"from":"kiosk","body":message,"level":level,"timestamp":ts}
    ret2 = requests.post(host,json=log)
    print("log: "+message)
    print(ret2)