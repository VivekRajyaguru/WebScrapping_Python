from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = raw_input('Enter Search Term:')
    dir_name = search.replace(" ", "_").lower()
    params = {"q": search, "tbm": "isch"}
    r = requests.get('https://www.google.co.in/search', params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    image = soup.findAll("div", {"id":"ires"})

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    for item in image:
        img_Objs = item.findAll("a")
        for imgs in img_Objs:
            try:
                img_Obj = requests.get(imgs.find("img").attrs["src"])
                print ("calling: ", imgs.find("img").attrs["src"])
                img_Name = imgs.parent.find("cite").attrs["title"].split(".")[0];
                try:
                    img = Image.open(BytesIO(img_Obj.content))
                    img.save("./"+ str(dir_name) +"/"+str(img_Name)+".jpeg")
                except:
                    print ("Could not Save Image")
            except:
                print ("Could not Call Image")

    StartSearch() #to make function recursive

StartSearch() #for Calling first Time