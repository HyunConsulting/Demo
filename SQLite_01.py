import requests
from bs4 import BeautifulSoup
import re
import sqlite3

fdic = {}
list_a = []
list_b = []

for page in range(1, 55):
    url = "https://fine.fss.or.kr/fine/fnctip/fncDicary/list.do?menuNo=900021&pageIndex="+str(page)
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ul = soup.select_one('ul.bd-list result-list')
        ul = soup.find('div','bd-list result-list')
        sub = ul.select('dl > dt')
        con = ul.select('dl > dd')

        for i in sub:
            tmp = i.get_text().strip()
            # tmp = tmp.replace("\r\n\t\t\t\t\t\t\t\t\xa0", "")
            tmp = re.sub('^[0-9]+. ', '', tmp)
            list_a.append(tmp)

        for i in con:
            tmp = i.get_text().strip()
            list_b.append(tmp)

        
    else:
        print(response.status_code)

for i in range(len(list_a)):
    fdic[i] = [list_a[i], list_b[i]]

conn = sqlite3.connect("D:\Data\SQLite\data01.db")
cur = conn.cursor()
conn.execute("create table if not exists fss_dic(id integer, name text, content text)")

for i in fdic:
    name = fdic[i][0]
    content = fdic[i][1]

    sql = "insert into fss_dic values (?, ?, ?)"
    cur.execute(sql, (i, name, content))

conn.commit()
conn.close()
