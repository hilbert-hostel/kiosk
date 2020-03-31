import requests
import datetime as dt

h = "https://hilbert.himkwtn.me/checkin"

def gather_info(cr,resv_info):
    cr.read_card()
    nw = dt.datetime.now()
    nw = nw.strftime("%Y-%m-%d")
    host = h
    params = {"nationalID":cr.card_data["nationalID"],"date":nw}
    ret = requests.get(host,params)
    temp = dict(ret.json())
    for i in temp:
        resv_info[i] = temp[i]

def request_OTP(resv_info,refn):
    host = (h+"/generate-otp/{}").format(resv_info["id"])
    ret = requests.post(host)
    temp = dict(ret.json())
    for i in temp:
        refn[i] = temp[i]
    print(refn)
    
def verify_OTP(resv_info,otp,token):
    host = h+"/verify-otp/{}".format(resv_info["id"])
    notp = ""
    for i in otp:
        notp += str(i)    
    body = {'otp':notp}
    ret = requests.post(host,json = body)
    temp = dict(ret.json())
    for i in temp:
        token[i] = temp[i]
    print(token)

def send_data(cr):
    host = h
    ret = requests.post(host,files = cr.card_data)
    print(ret)
