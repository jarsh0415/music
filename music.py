from bs4 import BeautifulSoup
import requests
import json
import time

response = requests.get(<<API>>)
soup = BeautifulSoup(response.text, 'html.parser')
load_data = json.loads(soup.prettify())
a=0
name_wrong = []
url_wrong = []
for i in load_data:
    if a%30!=0:
        time.sleep(3)
    a=a+1
    try:
        response = requests.get(i.get("url").replace('amp;','')).content

        f = open('D:/jarsh/music/jap/{}.mp3'.format(i.get("title")), 'wb')
        f.write(response)
        f.close()
    except:
        name_wrong.append(i.get("title"))
        url_wrong.append(i.get("url"))
print("finish!!")
