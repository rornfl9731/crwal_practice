from bs4 import BeautifulSoup
import requests
import urllib.request as req
import urllib.parse as rep
import os
from fake_useragent import UserAgent


opener =req.build_opener()
opener.addheaders = [('User-agent',UserAgent().ie)]
req.install_opener(opener)


r = 'https://gall.dcinside.com/board/lists?id=skwyverns'

res = req.urlopen(r)



soup = BeautifulSoup(res,'html.parser')

img_list = soup.select('tr.ub-content.us-post > td.gall_tit.ub-word > a ')




for i,k in enumerate(img_list,1):
    if k.text.startswith('[') == False:

        print(str(i)+". "+ k.text)












