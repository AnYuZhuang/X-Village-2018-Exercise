import requests
import json
url="https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5"

response=requests.get(url)
new_data=json.loads(response.text)
#print(len(new_data))                   #檢查list中有幾個dict

f=open('music.text','r+', encoding = 'utf8')               #寫入檔案music.text
for i in range(0,108):
    f.write(new_data[i]['title'])
    f.write(new_data[i]['startDate']+'~')
    f.write(new_data[i]['endDate']+'\n')
