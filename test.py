


"""

Android
iPhone

"""
import random
import time

import requests
from lxml import etree

from spider_instance import pc_UA, phone_UA, pc_UA, phone_UA, phone_NO

s = '''
Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 Maxthon/3235

'''
'Mobile'


def getHTMLText(ua):
    # url = 'https://www.so.com'
    url = 'https://www.baidu.com/'
    headers = {
        'User-Agent': ua,
        # "Cookie": "cookieStr"
    }

    try:
        # response = requests.get(url, params=param, proxies=proxies, verify=False, cookies=None)
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        # return response.text
        return response
    except:
        print('失败')
        return None


if __name__ == '__main__':
    # url = 'https://www.so.com',  # "//*[@id="bd_tabnav"]"   # 手机'//*[@id="scroller"]/ul[1]'

    with open('useragent.py', 'w') as f2:
        f2.write('\nUA = [\n')
        num = 0
        for ua in phone_NO.UA:
            response = getHTMLText(ua)
            if response:
                try:
                    html = etree.HTML(response.text)
                    # with open('xx.html', 'w') as f:
                    #     f.write(response.text)
                    # res = html.xpath('//*[@id="bd_tabnav"]|//*[@id="so-nav-tabs"]')
                    res = html.xpath('//*[@id="userinfo-wrap"]')  # 手机 '//*[@id="userinfo-wrap"]/a
                    if res:
                        print('成功:', num)
                        f2.write(f"\t'{ua}',\n")
                        num += 1
                    else:
                        print('没找到元素')
                except:
                    pass
            time.sleep(round(random.uniform(1, 1.7)))
        f2.write(']')

    # with open('phone_NO.py', 'w') as f2:
    #     f2.write('\nUA = [\n')
    #
    #     for ua in phone_UA.UA:
    #         if ua not in phone_UA_ok.UA:
    #             f2.write(f"\t'{ua}',\n")
    #
    #     f2.write(']')
