from urllib.request import Request
from urllib.request import urlopen
import re
import Logger
import time


class RentHouseInfo:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

def getHtml(url):
    req = Request(url)  
    req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')  
    req.add_header("Cookie",'suid=6812129920; yfx_c_g_u_id_10000001=_ck17071714412919812337032095317; yfx_mr_f_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%25e5%2593%2581%25e4%25b8%2593%25e6%25a0%2587%25e9%25a2%2598%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25e5%2593%2581%25e4%25b8%2593%25e6%25a0%2587%25e9%25a2%2598%3A%3Abzclk.baidu.com%3A%3A%3A%3Apmf_from_adv%3A%3A%25e5%2593%2581%25e4%25b8%2593%25e6%25a0%2587%25e9%25a2%2598; BIGipServer=3848866314.20480.0000; PHPSESSID=9ci3tamk6sujc7r97q0irkc034; yfx_f_l_v_t_10000001=f_t_1500273689981__r_t_1500273689981__v_t_1500276689747__r_c_0; yfx_mr_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%25e5%2593%2581%25e4%25b8%2593%25e6%25a0%2587%25e9%25a2%2598%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25e5%2593%2581%25e4%25b8%2593%25e6%25a0%2587%25e9%25a2%2598%3A%3Abzclk.baidu.com%3A%3A%3A%3Apmf_from_adv%3A%3A%25e5%2593%2581%25e4%25b8%2593%25e6%25a0%2587%25e9%25a2%2598; yfx_key_10000001=%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6; _va_ref=%5B%22%E5%93%81%E4%B8%93%E6%A0%87%E9%A2%98%22%2C%22%E5%93%81%E4%B8%93%E6%A0%87%E9%A2%98%22%2C1500276690%2C%22http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7wRKC07iFm0KFRQ00NgAku000005JgdW300000X1Wx2g.THLrYoa81V2tY6K85yF9pywdpAqVuNqsusK15ynLP1I9uHRsnj0snA7WnW00IHY3fHnsfbwDfRD1P1wDrjwKPDf4P177wbwAwbcvrRfsr0K95gTqFhdWpyfqn10srjnkrjDdriusThqbpyfqnHm0uHdCIZwsrBtEmhC8PybdpB4WUvYE5LNYUNq1ULNzmvRqmh7GuZRhIgwVgvd-uA-dUHdsTZGkFMNYUNqYugFV5iN-PiR4nzR3niN-PaNBraR4nzN-PBN9naR3PzN-riN9nBR4raudIAdxmvq8IAN8IjY-uHR-rHn-rjD-uHf-mW6-rHn-uHm-mH0-rjT-uHb-mHc-rH6hIgwVgvP9UgK9pyI85iN-PiR4nzR3niN-PaNBraR4nzN-PBN9naR3PzN-riN9nBR4rau_pLNV5HcL0APzm1Y1nW6dP6%26tpl%3Dtpl_10144_15654_1%26l%3D1054251002%26attach%3Dlocation%3D%26linkName%3D%25E6%25A0%2587%25E9%25A2%2598%26linkText%3D%25E6%2588%2591%25E7%2588%25B1%25E6%2588%2591%25E5%25AE%25B6%25EF%25BC%258C%25E5%2585%25A8%25E5%25BF%2583%25E5%2585%25A8%25E6%2584%258F%25E6%2589%25BE%25E6%2588%25BF%25EF%25BC%258C%25E7%259C%259F%25E5%25BF%2583%25E5%25AE%259E%25E6%2584%258F%26xp%3Did(%2522m77168413%2522)%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B1%255D%252FH2%255B1%255D%252FA%255B1%255D%26linkType%3D%26checksum%3D79%26wd%3D%E6%88%91%E7%88%B1%E6%88%91%E5%AE%B6%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1718%22%5D; __utmt=1; __utmt_t2=1; renthistorys=%5B%7B%22id%22%3A%22164075043%22%2C%22imgurl%22%3A%22house%5C%2F3815%5C%2F38155421%5C%2Fshinei%5C%2Fcafjocbdb639374d.jpg%22%2C%22housetitle%22%3A%22%5Cu9890%5Cu6167%5Cu4f73%5Cu56ed+3%5Cu5ba41%5Cu53852%5Cu536b133.7%5Cu5e73%5Cu7c73%22%2C%22parentareaname%22%3A%22%5Cu66d9%5Cu5149%22%2C%22buildarea%22%3A%22133.7%22%2C%22hallhouse%22%3A%223%5Cu5ba41%5Cu5385%22%2C%22districtname%22%3A%22%5Cu6d77%5Cu6dc0%22%2C%22conmmunityname%22%3A%22%5Cu9890%5Cu6167%5Cu4f73%5Cu56ed%22%2C%22price%22%3A%2212800%22%2C%22onePrice%22%3A957367%7D%2C%7B%22id%22%3A%22164121621%22%2C%22imgurl%22%3A%22house%5C%2F3815%5C%2F38151733%5C%2Fshinei%5C%2Findkfhhdb5d6d298.jpg%22%2C%22housetitle%22%3A%22%5Cu5b8f%5Cu6c47%5Cu56ed+2%5Cu5ba41%5Cu53851%5Cu536b53.2%5Cu5e73%5Cu7c73%22%2C%22parentareaname%22%3A%22%5Cu65b0%5Cu91d1%5Cu878d%5Cu8857%22%2C%22buildarea%22%3A%2253.2%22%2C%22hallhouse%22%3A%222%5Cu5ba41%5Cu5385%22%2C%22districtname%22%3A%22%5Cu897f%5Cu57ce%22%2C%22conmmunityname%22%3A%22%5Cu5b8f%5Cu6c47%5Cu56ed%22%2C%22price%22%3A%229000%22%2C%22onePrice%22%3A1691729%7D%2C%7B%22id%22%3A%22163631892%22%2C%22imgurl%22%3A%22house%5C%2F3767%5C%2F37672174%5C%2Fshinei%5C%2Fchhmbape532cc0c7.JPG%22%2C%22housetitle%22%3A%22%5Cu957f%5Cu9633%5Cu534a%5Cu5c9b%5Cu7965%5Cu4e91%5Cu88571%5Cu53f7%5Cu9662+2%5Cu5ba41%5Cu53851%5Cu536b%22%2C%22parentareaname%22%3A%22%5Cu957f%5Cu9633%5Cu534a%5Cu5c9b%5Cu5357%22%2C%22buildarea%22%3A%2289%22%2C%22hallhouse%22%3A%222%5Cu5ba41%5Cu5385%22%2C%22districtname%22%3A%22%5Cu623f%5Cu5c71%22%2C%22conmmunityname%22%3A%22%5Cu957f%5Cu9633%5Cu534a%5Cu5c9b%5Cu7965%5Cu4e91%5Cu88571%5Cu53f7%5Cu9662%22%2C%22price%22%3A%223900%22%2C%22onePrice%22%3A438202%7D%2C%7B%22id%22%3A%22164016452%22%2C%22imgurl%22%3A%22house%5C%2F3816%5C%2F38169982%5C%2Fshinei%5C%2Fkebnjelmcb22baed.jpg%22%2C%22housetitle%22%3A%22%5Cu7406%5Cu5de5%5Cu9644%5Cu4e2d%5Cu5bb6%5Cu5c5e%5Cu697c+2%5Cu5ba41%5Cu53851%5Cu536b%22%2C%22parentareaname%22%3A%22%5Cu5317%5Cu6d3c%5Cu8def%22%2C%22buildarea%22%3A%2257.16%22%2C%22hallhouse%22%3A%222%5Cu5ba41%5Cu5385%22%2C%22districtname%22%3A%22%5Cu6d77%5Cu6dc0%22%2C%22conmmunityname%22%3A%22%5Cu7406%5Cu5de5%5Cu9644%5Cu4e2d%5Cu5bb6%5Cu5c5e%5Cu697c%22%2C%22price%22%3A%226800%22%2C%22onePrice%22%3A1189643%7D%5D; _pzfxuvpc=1500273690260%7C8301901975409060073%7C25%7C1500276703134%7C2%7C6009042815426301517%7C1044097636508483955; _pzfxsvpc=1044097636508483955%7C1500276689992%7C5%7Chttp%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7wRKC07iFm0KFRQ00NgAku000005JgdW300000X1Wx2g.THLrYoa81V2tY6K85yF9pywdpAqVuNqsusK15ynLP1I9uHRsnj0snA7WnW00IHY3fHnsfbwDfRD1P1wDrjwKPDf4P177wbwAwbcvrRfsr0K95gTqFhdWpyfqn10srjnkrjDdriusThqbpyfqnHm0uHdCIZwsrBtEmhC8PybdpB4WUvYE5LNYUNq1ULNzmvRqmh7GuZRhIgwVgvd-uA-dUHdsTZGkFMNYUNqYugFV5iN-PiR4nzR3niN-PaNBraR4nzN-PBN9naR3PzN-riN9nBR4raudIAdxmvq8IAN8IjY-uHR-rHn-rjD-uHf-mW6-rHn-uHm-mH0-rjT-uHb-mHc-rH6hIgwVgvP9UgK9pyI85iN-PiR4nzR3niN-PaNBraR4nzN-PBN9naR3PzN-riN9nBR4rau_pLNV5HcL0APzm1Y1nW6dP6%26tpl%3Dtpl_10144_15654_1%26l%3D1054251002%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E6%252588%252591%2525E7%252588%2525B1%2525E6%252588%252591%2525E5%2525AE%2525B6%2525EF%2525BC%25258C%2525E5%252585%2525A8%2525E5%2525BF%252583%2525E5%252585%2525A8%2525E6%252584%25258F%2525E6%252589%2525BE%2525E6%252588%2525BF%2525EF%2525BC%25258C%2525E7%25259C%25259F%2525E5%2525BF%252583%2525E5%2525AE%25259E%2525E6%252584%25258F%2526xp%253Did(%252522m77168413%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D79%26wd%3D%25E6%2588%2591%25E7%2588%25B1%25E6%2588%2591%25E5%25AE%25B6%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1718; Hm_lvt_0bccd3f0d70c2d02eb727b5add099013=1500273690,1500276690; Hm_lpvt_0bccd3f0d70c2d02eb727b5add099013=1500276703; Hm_lvt_fbfca6a323fa396dde12616e37bc1df9=1500273690,1500276690; Hm_lpvt_fbfca6a323fa396dde12616e37bc1df9=1500276703; Hm_lvt_b3ad53a84ea4279d8124cc28d3c3220f=1500273690,1500276690; Hm_lpvt_b3ad53a84ea4279d8124cc28d3c3220f=1500276703; __utma=1.494549773.1500273690.1500273690.1500276690.2; __utmb=1.5.10.1500276690; __utmc=1; __utmz=1.1500276690.2.2.utmcsr=baidu|utmccn=åä¸æ é¢|utmcmd=ppzq|utmctr=åä¸æ é¢|utmcct=åä¸æ é¢; __utma=228451417.1886254156.1500273690.1500273690.1500276690.2; __utmb=228451417.5.10.1500276690; __utmc=228451417; __utmz=228451417.1500276690.2.2.utmcsr=baidu|utmccn=åä¸æ é¢|utmcmd=ppzq|utmctr=åä¸æ é¢|utmcct=åä¸æ é¢; _va_id=9d9fc13a285fac02.1500273690.2.1500276703.1500276690.; _va_ses=*; domain=bj')
    try:
        page = urlopen(req,timeout=3)
        html = page.read()
    except :
        try:
            time.sleep(2)
            page = urlopen(req,timeout=3)
            html = page.read()
        except :
            time.sleep(2)
            page = urlopen(req,timeout=3)
            html = page.read()
        pass
    pass
   
    try:
        html = html.decode()
    except :
        html = html.decode('GBK')
    pass
    return html

def getUrl(html):
    reg = r'<h2><a href="/rent/([0-9]*?)" target="_blank">'    
    urlre = re.compile(reg)     
    urllist = re.findall(urlre,html)      
    for url in urllist:
        try:
            getInfo(r"http://bj.5i5j.com/rent/" + url)
        except Exception as e :
            try:
               Logger.writeErrorLog(str(e.args[0]))
               Logger.writeErrorLog("Url:" + url)
            except :
               Logger.writeErrorLog("未知错误")
               Logger.writeErrorLog("Url:" + url)
            pass
        pass
       
def getInfo(url):
    html = getHtml(url)

   
    rentHouseInfo = RentHouseInfo()
    #获取小区
    estateMatch = re.search(r'var communityAddress = "(.*?)"', html, re.M | re.I)
    if estateMatch is None:
        rentHouseInfo.estate = ''
    else:
        rentHouseInfo.estate = estateMatch.group(1)

  
    #获取面积
    areaMatch = re.search(r'<li><b>面积：</b>(.*?)平米</li>', html, re.M | re.I)
    if areaMatch is None:
        rentHouseInfo.aera = ''
    else:
        rentHouseInfo.aera = areaMatch.group(1)

    #获取户型
    hxMatch = re.search(r'<b>户型：</b>(.*?)&nbsp', html, re.M | re.I)
    if hxMatch is None:
        rentHouseInfo.hx = ''
    else:
        rentHouseInfo.hx = hxMatch.group(1)

    #获取楼层
    lcMatch = re.search(r'<b>楼层：</b>(.*?)</li>', html, re.M | re.I)
    if lcMatch is None:
        rentHouseInfo.lc = ''
    else:
        rentHouseInfo.lc = lcMatch.group(1)

    #获取朝向
    cxMatch = re.search(r'<li><b>朝向：</b>(.*?)</li>', html, re.M | re.I)
    if cxMatch is None:
        rentHouseInfo.cx = ''
    else:
        rentHouseInfo.cx = cxMatch.group(1)

    #获取价格
    priceMatch = re.search(r'<span class="font-price">(.*?)</span>', html, re.M | re.I)
    if priceMatch is None:
        rentHouseInfo.price = ''
    else:
        rentHouseInfo.price = priceMatch.group(1)

    #获取经度
    jdMatch = re.search(r'var mapX ="(.*?)"', html, re.M | re.I)
    if jdMatch is None:
        rentHouseInfo.jd = ''
    else:
        rentHouseInfo.jd = jdMatch.group(1)

     #获取维度
    wjdMatch = re.search(r'var mapY ="(.*?)"', html, re.M | re.I)
    if wjdMatch is None:
        rentHouseInfo.wd = ''
    else:
        rentHouseInfo.wd = wjdMatch.group(1)

    #获取房屋编号
    houseidMatch = re.search(r'var houseid = "(.*?)"', html, re.M | re.I)
    if houseidMatch is None:
        rentHouseInfo.houseid = ''
    else:
        rentHouseInfo.houseid = houseidMatch.group(1)

        
    #获取租赁方式
    zlfsdMatch = re.search(r'<span class="mr-r">(.*?)</span>', html, re.M | re.I)
    if zlfsdMatch is None:
        rentHouseInfo.zlfs = ''
    else:
        rentHouseInfo.zlfs = zlfsdMatch.group(1)

    

    file.writelines(rentHouseInfo.houseid + '\t' + rentHouseInfo.jd + '\t' + rentHouseInfo.wd + '\t' + rentHouseInfo.estate + '\t' + rentHouseInfo.aera + '\t' + rentHouseInfo.hx + '\t' + rentHouseInfo.zlfs + '\t' + rentHouseInfo.lc + '\t' + rentHouseInfo.cx + '\t' + rentHouseInfo.price + '\t\r\n')
    file.flush()
    print(rentHouseInfo.houseid)

if __name__ == '__main__':
    url = ''
    try:
        file = open(r'D:\O\Data\Woaiwojia\info.txt',"a")
        pageNum = 1
        #swithCate = False
        while(True):
            url = "http://bj.5i5j.com/rent/n" + str(pageNum) 
            print(url)
            html = getHtml(url)
            #validre = re.search(r'请选出以下倒置的房屋图片',html, re.M | re.I)
            #if(validre != None):
            #    Logger.writeInfoLog("Current Url is:" + url)
            #    webbrowser.open_new(url)
            #    break;
            #reobj = re.search(r'没有找到相关内容',html, re.M | re.I)
            #if(reobj != None):
            #    if(swithCate == True):
            #        break
            #    else:
            #        cateNum = cateNum + 1
            #        swithCate = True
            #        pageNum = 1
            #else:
            #swithCate = False
            getUrl(html)
            pageNum = pageNum + 1
       
    except Exception as e :
        Logger.writeErrorLog("Current Url is:" + url)
        Logger.writeErrorLog(str(e.args[0]))
    finally:
         file.close()
    