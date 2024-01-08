import requests

serviceKey = "AGWla5CTAUquQEH8OP4H9joW2h9tYIj7NmhPs8MR1O3XI7G%2BEgRJZ%2FoizD0b9QHzI3FdQ6wPMRzvq8O%2Ft%2FAoxQ%3D%3D"
areaCd = "1"
# url = "https://openapi.kpx.or.kr/openapi/smp1hToday/getSmp1hToday"
url = "https://openapi.kpx.or.kr/openapi/smp1hToday/getSmp1hToday?serviceKey=AGWla5CTAUquQEH8OP4H9joW2h9tYIj7NmhPs8MR1O3XI7G%2BEgRJZ%2FoizD0b9QHzI3FdQ6wPMRzvq8O%2Ft%2FAoxQ%3D%3D&areaCd=1"
params = {'serviceKey':serviceKey, 'areaCd':areaCd}

# response = requests.get(url,params=params)
response = requests.get(url=url)
# print(response.text)

import xml.etree.ElementTree as ET

root = ET.fromstring(response.content)
tree = ET.ElementTree(root)
tree.write('response.xml',encoding='utf-8')

import csv
with open('response.csv','w',newline='') as csv_file:
    writer = csv.wirter(csv_file)
    header=[]
    root_h=root[1][0]
    for x in root_h[0]:
        header.append(x.tag)
    writer.writerow(header)
    for item in root_h:
        row = []
        for child in item:
            row.append(child.text)
        writer.writerow(row)
