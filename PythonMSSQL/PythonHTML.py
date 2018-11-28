import urllib.request
import re
import chardet


def getHtml(url):
    page = urllib.request.urlopen(url)  
    html = page.read()
    try:
        html = html.decode()
    except :
        html = html.decode('GBK')
    pass
   
    
    return html



def getImg(html):
    reg = r'src="(.+?\.jpg)"'    
    imgre = re.compile(reg)     
    imglist = re.findall(imgre,html)      

    x = 0 

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'D:\E\%s.jpg' % x)
        x+=1

html = getHtml("http://www.163.com/")
getImg(html)