
import requests
import csv
from requests.api import head

service_key = "82c3c014-aad8-4c35-91d6-6b3187cff505"

url = 'http://api.coincap.io/v2/assets'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response = requests.request("GET",url,headers=headers,data={})
myjson = response.json()
ourdata = []
csvheader = ['SYMBOL','NAME','PRICE_USD']

for x in myjson['data']:
    listing = [x['symbol'],x['name'],x['priceUsd']]
    ourdata.append(listing)

with open('D:\Data\CSV\\coin01.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)
    
print('done')