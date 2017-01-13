#coding:utf-8

import requests
from lxml import  etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


url=' http://www.budejie.com/1'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
text=requests.get(url,headers=header).content

selector=etree.HTML(text)
b='/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/div[1]/@data-mp4' % (2, 1)
video = selector.xpath(b)

print video
