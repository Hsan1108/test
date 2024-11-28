import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#from urlparse import urljoin # 這行似乎沒有使用到

url = 'https://new.ntpu.edu.tw/compilation-of-regulations'
html = requests.get(url)
html.encoding='utf-8'


sp = BeautifulSoup(html.text, features="lxml")

pdf_dir="pdfs/"
if not os.path.exists(pdfs_dir):
    os.mkdir(pdfs_dir)
    
links=sp.find_all("a")
for link in links:
    href=link.get("herf")
    attrs=[href]
    if href != None and hret.startswitch("https://"):
        full_path = attr
        filename = full_path.split('/')[-1]
        print(full_path)
        try:
            pdf = urlopen(full_path)
            f = open(os.path.join(pdf_dir,filename),'wb')
            f.write(pdf.read())
            f.close()
        except:
            print("{} 無法讀取".format(filename))
            
'''
links=sp.find_all("a")
for link in links:
	href=link.get("href")
	#不用再多一層 attr 迴圈，href 已經是連結了
	
	#如果不是 .pdf 結尾，直接跳過不處理
	if(href == None or href.split('.')[-1]!='pdf'):
		continue;
	
	#關於網址的處理
	if(href[0:4]=='http'):
		full_path = href
	elif(href[0]=='/'): #這邊要處理開頭為 / 的網址
		full_path = "http://academic.ntue.edu.tw" + href
	else: #其他的是相對路徑
		full_path= "http://academic.ntue.edu.tw/files/" + href
	print(full_path)
	
	#後面就是抓 full_path 並儲存
'''