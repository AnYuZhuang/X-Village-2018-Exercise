import json            #7/19 API＆Web Crawler  ex1.1
import requests
from requests_html import HTMLSession
session=HTMLSession()
url='https://www.metaweather.com/api/location/2306179/2018/7/18/'

imfo=requests.get(url)
data=json.loads(imfo.text)
print(data)
