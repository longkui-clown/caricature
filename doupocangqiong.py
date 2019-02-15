#coding=utf-8
import urllib.request
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  

x = 1
y = 1
max_util = 1000
max_page = 50
index = 1
for i in range(1, max_util):
  for j in range(1, max_page):
    imgurl = "http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%E6%8B%86%E5%88%86%E7%89%88%2F" + str(i) + "%E8%AF%9D%2F" + str(j) + ".jpg-zymk.high.webp"
    print(imgurl)
    #status = urllib.request.urlopen(imgurl).code
    try: 
      req = urllib.request.Request(url=imgurl, headers=headers)  
      status = urllib.request.urlopen(req).code
      print(status)
      if status == 200:
          urllib.request.urlretrieve(imgurl,'%s.jpg' % index)
          index = index + 1
    except:  
      print(index)
      break
      
      