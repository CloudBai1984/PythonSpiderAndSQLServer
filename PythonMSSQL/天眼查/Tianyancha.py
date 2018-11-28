from urllib.request import Request
from urllib.request import urlopen
import urllib
import re
import chardet
import Logger
import webbrowser
import sys
import codecs
import tkinter.messagebox
from tkinter import *


class RentHouseInfo:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)




def getHtml(url):
    req = Request(url)  
    req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')  
    req.add_header("Cookie",'TYCID=5c9548906b8111e79631b9346b1d1640; uccid=3ffb3f1db64073e8fb9f754486a1750b; ssuid=6349433400; aliyungf_tc=AQAAAP5v82kGgw4AuAf5cirHDwsUg2Bi; csrfToken=s12gInDYBh7QQbMRda5KJkmN; token=69a784aa48b047e281fe0ba8ea0008dd; _utm=cd55c0954e184886b1e564fd10e1300d; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzgxMTM5MzU5NyIsImlhdCI6MTUwNzk3MDczNSwiZXhwIjoxNTIzNTIyNzM1fQ.dJ0uouTF2uXdOCIqFsB9Sry4TX-WslXLbd3PJaWwMW8PqcrbIC2ZkLI1x82buLNxGpiR7S8y0e59M5vm2s-9-w%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213811393597%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzgxMTM5MzU5NyIsImlhdCI6MTUwNzk3MDczNSwiZXhwIjoxNTIzNTIyNzM1fQ.dJ0uouTF2uXdOCIqFsB9Sry4TX-WslXLbd3PJaWwMW8PqcrbIC2ZkLI1x82buLNxGpiR7S8y0e59M5vm2s-9-w; OA=TYuvIXze/y9nJ81kb/nOgxLBymOdSIh0OH43yFNZfqQ=; _csrf=ik1Jydy+Gb8DFGNBO5J1ew==; _csrf_bk=65166444cc395f9891eef9f2b99d70d7; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1505973152,1507967659,1507967686,1507969058; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1507970779')
    page = urlopen(req)
  
    html = page.read()
    try:
        html = html.decode()
    except :
        html = html.decode('GBK')
    pass
    return html

def getUrl(html):
    reg = r'<div class="search_right_item"><div><a href="(.*?)"'    
    urlre = re.compile(reg)     
    urllist = re.findall(urlre,html)      
    if(len(urllist) == 0):
        tkinter.messagebox.showinfo("Info","需要校验")
        Logger.writeErrorLog("Html:\r\n" + html)
      
        raise Exception("需要校验");
    for url in urllist:
        try:
            getInfo(url)
        except Exception as e :
             Logger.writeErrorLog(e.args[0])
             Logger.writeErrorLog("Url:" + url)
        pass
       
def getInfo(url):
    html = getHtml(url)
    m = re.search(r'https://www.tianyancha.com/company/(.*)',url,0)
    f = codecs.open("d:\\O\\log\\tianyancha\\data\\" + m.group(1) + ".html", 'w', 'UTF-8')
    f.write(html)
    f.close()
    print(url)

if __name__ == '__main__':
    url = ''
    try:
        pageNum = 6
        cateNum = 10
        hxNum = 1
        swithCate = False
        while(True):
            url = "https://jx.tianyancha.com/search/p" + str(pageNum)
            print(url)
            html = getHtml(url)
            getUrl(html)
            pageNum = pageNum + 1
       
    except Exception as e :
        webbrowser.open_new(url);
        Logger.writeErrorLog("Current Url is:" + url)
        Logger.writeErrorLog(e.args[0])
    