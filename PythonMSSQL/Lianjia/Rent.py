from urllib.request import Request
from urllib.request import urlopen
import re
import chardet
import Logger
import webbrowser


class RentHouseInfo:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)




def getHtml(url):
    req = Request(url)  
    req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')  
    req.add_header("Cookie",'zufang_huodong_show=1; lianjia_uuid=a41e5746-ba9b-409b-b759-478e48698f41; UM_distinctid=15d35ea2441201-070b8ece7c57bf-3e64430f-113b85-15d35ea24422d5; select_city=110000; _jzqckmp=1; _jzqy=1.1499848124.1500259783.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; all-lj=c28812af28ef34a41ba2474a2b5c52c2; _smt_uid=5965de1b.22415966; CNZZDATA1253477573=1417729210-1499845563-null%7C1500265357; CNZZDATA1254525948=782817789-1499847470-null%7C1500262550; CNZZDATA1255633284=1110144854-1499846383-null%7C1500263902; CNZZDATA1255604082=611895875-1499847291-null%7C1500261752; _qzja=1.2062560826.1499848125180.1500260672091.1500261529702.1500265705061.1500265727287.0.0.0.100.7; _qzjb=1.1500256271636.72.0.0.0; _qzjc=1; _qzjto=72.6.0; _jzqa=1.2532091371107936000.1499848124.1500260672.1500261530.7; _jzqc=1; _jzqb=1.41.10.1500261530.1; _ga=GA1.2.435082923.1499848134; _gid=GA1.2.1073622480.1500256275; lianjia_ssid=2df61eb2-69ea-4e27-af66-091e879114e5')
    page = urlopen(req)
  
    html = page.read()
    try:
        html = html.decode()
    except :
        html = html.decode('GBK')
    pass
    return html

def getUrl(html):
    reg = r'<div class="pic-panel"><a target="_blank" href="(.*?)"><img'    
    urlre = re.compile(reg)     
    urllist = re.findall(urlre,html)      
    for url in urllist:
        try:
            getInfo(url)
        except Exception as e :
             Logger.writeErrorLog(e.args[0])
             Logger.writeErrorLog("Url:" + url)
        pass
       
def getInfo(url):
    html = getHtml(url)

    #获取位置
    locationMatch = re.search(r'<p><i>位置：</i>(.*?)</p>', html, re.M | re.I)
    if locationMatch is not None:
        reglocation = r'<a href=".*?">(.*?)</a>'
        lctre = re.compile(reglocation)     
    
        lctlist = re.findall(lctre,locationMatch.group(1))   
    
        rentHouseInfo = RentHouseInfo()
        rentHouseInfo.location = ''

        for lct in lctlist:   
            rentHouseInfo.location = rentHouseInfo.location + lct 

    #获取小区
    estateMatch = re.search(r'<p><i>小区：</i><a href=".*?">(.*?)</a>', html, re.M | re.I)
    if estateMatch is None:
         rentHouseInfo.estate = ''
    else:
        rentHouseInfo.estate = estateMatch.group(1)

    #获取地铁
    subwayMatch = re.search(r'<p><i>地铁：</i>(.*?)</p>', html, re.M | re.I)
    if subwayMatch is None:
        rentHouseInfo.subway = ''
    else:
        rentHouseInfo.subway = subwayMatch.group(1)

    #获取面积
    areaMatch = re.search(r'<p class="lf"><i>面积：</i>(.*?)平米.*?</p>', html, re.M | re.I)
    if areaMatch is None:
        rentHouseInfo.aera = ''
    else:
        rentHouseInfo.aera = areaMatch.group(1)

    #获取户型
    hxMatch = re.search(r'<p class="lf"><i>房屋户型：</i>(.*?)</p>', html, re.M | re.I)
    if hxMatch is None:
        rentHouseInfo.hx = ''
    else:
        rentHouseInfo.hx = hxMatch.group(1)

    #获取楼层
    lcMatch = re.search(r'<p class="lf"><i>楼层：</i>(.*?)</p>', html, re.M | re.I)
    if lcMatch is None:
        rentHouseInfo.lc = ''
    else:
        rentHouseInfo.lc = lcMatch.group(1)

    #获取朝向
    cxMatch = re.search(r'<p class="lf"><i>房屋朝向：</i>(.*?)</p>', html, re.M | re.I)
    if cxMatch is None:
        rentHouseInfo.cx = ''
    else:
        rentHouseInfo.cx = cxMatch.group(1)

    #获取价格
    priceMatch = re.search(r'totalPrice:\'(.*?)\'', html, re.M | re.I)
    if priceMatch is None:
        rentHouseInfo.price = ''
    else:
        rentHouseInfo.price = priceMatch.group(1)

    #获取经纬度
    jwdMatch = re.search(r'resblockPosition:\'(.*?)\'', html, re.M | re.I)
    if jwdMatch is None:
        rentHouseInfo.jwd = ''
    else:
        rentHouseInfo.jwd = jwdMatch.group(1)

    #获取房屋编号
    houseidMatch = re.search(r'houseId:\'(.*?)\'', html, re.M | re.I)
    if houseidMatch is None:
        rentHouseInfo.houseid = ''
    else:
        rentHouseInfo.houseid = houseidMatch.group(1)

     #获取小区编号
    estateidMatch = re.search(r'resblockId:\'(.*?)\'', html, re.M | re.I)
    if estateidMatch is None:
        rentHouseInfo.estateid = ''
    else:
        rentHouseInfo.estateid = estateidMatch.group(1)
        
    #获取租赁方式
    zlfsdMatch = re.search(r'<span class="label">租赁方式：</span>(.*?)</li>', html, re.M | re.I)
    if zlfsdMatch is None:
        rentHouseInfo.zlfs = ''
    else:
        rentHouseInfo.zlfs = zlfsdMatch.group(1)

    

    file.writelines(rentHouseInfo.houseid + '\t' + rentHouseInfo.estateid + '\t' + rentHouseInfo.location + '\t' + rentHouseInfo.estate + '\t' + rentHouseInfo.subway + '\t' + rentHouseInfo.aera + '\t' + rentHouseInfo.hx + '\t' + rentHouseInfo.zlfs + '\t' + rentHouseInfo.lc + '\t' + rentHouseInfo.cx + '\t' + rentHouseInfo.price + '\t' + rentHouseInfo.jwd + '\t\r\n')
   
    print(rentHouseInfo.houseid)

if __name__ == '__main__':
    url = ''
    try:
        file = open(r'D:\O\Data\Lianjia\rp1.txt',"a")
        pageNum = 101
        cateNum = 10
        hxNum = 1
        swithCate = False
        while(True):
            url = "https://bj.lianjia.com/zufang/pg" + str(pageNum) + "rp" + str(cateNum) + "/"
            print(url)
            html = getHtml(url)
            validre = re.search(r'请选出以下倒置的房屋图片',html, re.M | re.I)
            if(validre != None):
                Logger.writeInfoLog("Current Url is:" + url)
                webbrowser.open_new(url)
                break;
            reobj = re.search(r'没有找到相关内容',html, re.M | re.I) 
            if(reobj != None):
                if(swithCate == True):
                    break
                else:
                    cateNum = cateNum + 1
                    swithCate = True
                    pageNum = 1
            else:
                swithCate = False
                getUrl(html)
                pageNum = pageNum + 1
       
    except Exception as e :
        Logger.writeErrorLog("Current Url is:" + url)
        Logger.writeErrorLog(e.args[0])
    finally:
         file.close()
    