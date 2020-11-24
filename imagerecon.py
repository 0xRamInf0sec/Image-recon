import requests
import pyfiglet
from bs4 import BeautifulSoup
ban=pyfiglet.figlet_format("IMAGE R3CON",font="slant")
print(ban)
print("                           created by Ramalingasamy M K")
print()
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
image=input(C+"Enter the image path : ")
try:
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    url='http://www.google.co.in/searchbyimage/upload'
    secondurl={'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
    response = requests.post(url, files=secondurl,allow_redirects=False)
    fetch=response.headers['Location']
    #print(fetch)
    req=requests.get(fetch,headers=headers)
    socialmedia=["instagram","facebook","twitter","linkedin","github"]
    linklist=[]
    print(G+"[+] Scan started......")
    print(G+"Checking whether the image is associated in any social media ")
    print(G+"Scanning started in Instagram")
    print(G+"Scanning started in Github")
    print(G+"Scanning started in Facebook")
    print(G+"Scanning started in Twitter")
    print(G+"Scanning started in Linkedin")           
    if(req.status_code == 200):
        
        soup = BeautifulSoup(req.content,'html.parser')
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if 'href' in str(anchors[0]):
                linklist.append(anchors[0]['href'])
                #print(linklist)
        c=0
        for i in socialmedia:
            sm=str(i)
            #print(sm)
            for j in linklist:
                if sm in str(j):
                    c=c+1
                    print(C+"[+]"+j)
        if c == 0:
            print(R+"No social Media links associated with this image")
except Exception as e:
    print(e)