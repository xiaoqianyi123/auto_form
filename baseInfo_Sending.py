import urllib.request,urllib.parse
import ssl
from urllib.parse import quote,unquote
ssl._create_default_https_context = ssl._create_unverified_context
import datetime

def upload_form():
        url = 'https://app.bupt.edu.cn/ncov/wap/default/save'
        headers = {
                'Host': 'app.bupt.edu.cn',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://app.bupt.edu.cn',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)  Mobile/15E148 wxwork/4.0.19 MicroMessenger/7.0.1 Language/zh ColorScheme/Light',
                'Connection': 'keep-alive',
                'Referer': 'https://app.bupt.edu.cn/ncov/wap/default/index',
                'Cookie': 'Hm_lpvt_48b682d4885d22a90111e46b972e3268=1667877460; Hm_lvt_48b682d4885d22a90111e46b972e3268=1667792547,1667799468,1667827796,1667865457; eai-sess=2unqk923k1amd4i3kq630cnok1; UUkey=80309d0ce3bc43b721bdc701603689c1'
        }
        # 模拟表单提交
        dict = {
                'jtzz': 'MIKA_Polar_test3',
        }
        str_data = 'ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&szgj=&szcs=&zgfxdq=0&mjry=0&csmjry=0&ymjzxgqk=&xwxgymjzqk=3&uid=79869&date=20221109&tw=2&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=%E6%97%A0&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E6%B5%B7%E6%B7%80%E6%A0%A1%E5%8C%BA&area=%E5%8C%97%E4%BA%AC%E5%B8%82++%E6%B5%B7%E6%B7%80%E5%8C%BA&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&geo_api_info=%7B%22type%22:%22complete%22,%22position%22:%7B%22Q%22:39.963110894098,%22R%22:116.356087782119,%22lng%22:116.356088,%22lat%22:39.963111%7D,%22location_type%22:%22html5%22,%22message%22:%22Get+geolocation+success.Convert+Success.Get+address+success.%22,%22accuracy%22:35,%22isConverted%22:true,%22status%22:1,%22addressComponent%22:%7B%22citycode%22:%22010%22,%22adcode%22:%22110108%22,%22businessAreas%22:%5B%7B%22name%22:%22%E5%8C%97%E4%B8%8B%E5%85%B3%22,%22id%22:%22110108%22,%22location%22:%7B%22Q%22:39.955976,%22R%22:116.33873,%22lng%22:116.33873,%22lat%22:39.955976%7D%7D,%7B%22name%22:%22%E5%B0%8F%E8%A5%BF%E5%A4%A9%22,%22id%22:%22110108%22,%22location%22:%7B%22Q%22:39.957147,%22R%22:116.364058,%22lng%22:116.364058,%22lat%22:39.957147%7D%7D,%7B%22name%22:%22%E8%A5%BF%E7%9B%B4%E9%97%A8%22,%22id%22:%22110102%22,%22location%22:%7B%22Q%22:39.942856,%22R%22:116.34666099999998,%22lng%22:116.346661,%22lat%22:39.942856%7D%7D%5D,%22neighborhoodType%22:%22%E7%A7%91%E6%95%99%E6%96%87%E5%8C%96%E6%9C%8D%E5%8A%A1;%E5%AD%A6%E6%A0%A1;%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1%22,%22neighborhood%22:%22%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%22,%22building%22:%22%22,%22buildingType%22:%22%22,%22street%22:%22%E8%A5%BF%E5%9C%9F%E5%9F%8E%E8%B7%AF%22,%22streetNumber%22:%2210%E5%8F%B7%22,%22country%22:%22%E4%B8%AD%E5%9B%BD%22,%22province%22:%22%E5%8C%97%E4%BA%AC%E5%B8%82%22,%22city%22:%22%22,%22district%22:%22%E6%B5%B7%E6%B7%80%E5%8C%BA%22,%22towncode%22:%22110108008000%22,%22township%22:%22%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%22%7D,%22formattedAddress%22:%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E6%B5%B7%E6%B7%80%E6%A0%A1%E5%8C%BA%22,%22roads%22:%5B%5D,%22crosses%22:%5B%5D,%22pois%22:%5B%5D,%22info%22:%22SUCCESS%22%7D&created=1667787577&sfzx=1&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=&fjsj=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&sfsfbh=0&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&sfjzxgym=1&sfjzdezxgym=1&id=24815020&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy='
        str_data = urllib.parse.parse_qs(str_data)
        str_data['date'] = ['20211111']
        str_data = {key: str_data[key][0] for key in str_data}
        print(str_data['date'])
        str_data['date'] = datetime.datetime.now().strftime('%Y%m%d')
        print(str_data)

        data = urllib.parse.urlencode(str_data).encode('utf-8')
        print(data)
        data1 = 'ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&szgj=&szcs=&zgfxdq=0&mjry=0&csmjry=0&ymjzxgqk=&xwxgymjzqk=3&uid=79869&date=20221117&tw=2&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=%E6%97%A0&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E6%B5%B7%E6%B7%80%E6%A0%A1%E5%8C%BA&area=%E5%8C%97%E4%BA%AC%E5%B8%82++%E6%B5%B7%E6%B7%80%E5%8C%BA&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&geo_api_info=%7B%22type%22:%22complete%22,%22position%22:%7B%22Q%22:39.963110894098,%22R%22:116.356087782119,%22lng%22:116.356088,%22lat%22:39.963111%7D,%22location_type%22:%22html5%22,%22message%22:%22Get+geolocation+success.Convert+Success.Get+address+success.%22,%22accuracy%22:35,%22isConverted%22:true,%22status%22:1,%22addressComponent%22:%7B%22citycode%22:%22010%22,%22adcode%22:%22110108%22,%22businessAreas%22:%5B%7B%22name%22:%22%E5%8C%97%E4%B8%8B%E5%85%B3%22,%22id%22:%22110108%22,%22location%22:%7B%22Q%22:39.955976,%22R%22:116.33873,%22lng%22:116.33873,%22lat%22:39.955976%7D%7D,%7B%22name%22:%22%E5%B0%8F%E8%A5%BF%E5%A4%A9%22,%22id%22:%22110108%22,%22location%22:%7B%22Q%22:39.957147,%22R%22:116.364058,%22lng%22:116.364058,%22lat%22:39.957147%7D%7D,%7B%22name%22:%22%E8%A5%BF%E7%9B%B4%E9%97%A8%22,%22id%22:%22110102%22,%22location%22:%7B%22Q%22:39.942856,%22R%22:116.34666099999998,%22lng%22:116.346661,%22lat%22:39.942856%7D%7D%5D,%22neighborhoodType%22:%22%E7%A7%91%E6%95%99%E6%96%87%E5%8C%96%E6%9C%8D%E5%8A%A1;%E5%AD%A6%E6%A0%A1;%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1%22,%22neighborhood%22:%22%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%22,%22building%22:%22%22,%22buildingType%22:%22%22,%22street%22:%22%E8%A5%BF%E5%9C%9F%E5%9F%8E%E8%B7%AF%22,%22streetNumber%22:%2210%E5%8F%B7%22,%22country%22:%22%E4%B8%AD%E5%9B%BD%22,%22province%22:%22%E5%8C%97%E4%BA%AC%E5%B8%82%22,%22city%22:%22%22,%22district%22:%22%E6%B5%B7%E6%B7%80%E5%8C%BA%22,%22towncode%22:%22110108008000%22,%22township%22:%22%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%22%7D,%22formattedAddress%22:%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E6%B5%B7%E6%B7%80%E6%A0%A1%E5%8C%BA%22,%22roads%22:%5B%5D,%22crosses%22:%5B%5D,%22pois%22:%5B%5D,%22info%22:%22SUCCESS%22%7D&created=1667787577&sfzx=1&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=&fjsj=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&sfsfbh=0&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&sfjzxgym=1&sfjzdezxgym=1&id=24815020&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy='
        data1 = data1.encode()
        print(data1)
        # data = 'jtzz=1234567%E6%B5%8B%E8%AF%95'
        req = urllib.request.Request(url=url, data=data, headers=headers)
        response = urllib.request.urlopen(req)
        page = response.read().decode('utf-8')
        print(page)
