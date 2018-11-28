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
import wx.html2


class RentHouseInfo:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)




def getHtml(url):
    req = Request(url)  
    req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')  
    req.add_header("Cookie",'cookieShowLoginTip=3; sid=s%3AcBUvRNoTM6hU_v2NCdGHBR4D9Va7rQI1.g%2ByZFGeiQjGbRvbXF%2Fa2kNug4WSJ5BnYKwVfyZz8Zz0; responseTimeline=40; _zg=%7B%22uuid%22%3A%20%2215f47409daf573-0e762a3fae41b8-3e64430f-113b85-15f47409db07dc%22%2C%22sid%22%3A%201509344172.159%2C%22updated%22%3A%201509348941.252%2C%22info%22%3A%201509344172163%2C%22cuid%22%3A%20%221c875253-10bd-45a9-95d7-778979eb85f3%22%7D; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1509348188,1509348810,1509348872,1509348899; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1509348942')
    page = urlopen(req)
  
    html = page.read()
    try:
        html = html.decode()
    except :
        html = html.decode('GBK')
    pass
    return html

def getUrl(html):
    reg = r'<div class="company-title"><a href="(.*?)" target="_blank" title="点击查看公司详情"'    
    urlre = re.compile(reg)     
    urllist = re.findall(urlre,html)      
    if(len(urllist) == 0):
        tkinter.messagebox.showinfo("Info","需要校验")
        Logger.writeErrorLog("Html:\r\n" + html)
        raise Exception("需要校验1")
    for url in urllist:
        try:
            getInfo("http://www.qixin.com" + url)
        except Exception as e :
             if("需要校验2" == e.args[0]):
                  tkinter.messagebox.showinfo("Info","检验")
                  getInfo("http://www.qixin.com" + url)
                  continue
             Logger.writeErrorLog(e.args[0])
             Logger.writeErrorLog("Url:" + url)
        pass
       
def getInfo(url):
    try:
        html = getHtml(url)
        m = re.search(r'<td>统一社会信用代码</td><td>(.*?)</td>',html,0)
        f = codecs.open("d:\\O\\log\\tianyancha\\data\\" + m.group(1) + ".html", 'w', 'UTF-8')
        f.write(html)
        f.close()
        print(url)
    except :
        webbrowser.open_new(url)
        raise Exception("需要校验2")
    pass


if __name__ == '__main__':
    url = ''
    try:
        pageNum = 4
        cateNum = 10
        hxNum = 1
        swithCate = False
        while(True):
            url = "http://www.qixin.com/search?area.province=14&page=" + str(pageNum)
            print(url)
            html = getHtml(url)
            try:
                getUrl(html)
                
            except :
                webbrowser.open_new(url)
                continue
            pass
            pageNum = pageNum + 1
    except Exception as e :
       
        Logger.writeErrorLog("Current Url is:" + url)
        Logger.writeErrorLog(e.args[0])
    