#coding:utf-8
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Crawler:
	def __init__(self,url):
		self.rooturl=url
		
	def getURL(self):           #return list
		urllist=[]
		for i in range(1,51):
			urllist.append(self.rooturl+str(i))
		return urllist
	
	def getHTML(self,url):      #return html(str) of each page
		header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
		html=requests.get(url,headers=header).content
		return html
		
	def getVideo(self,NHTML):    #obtain name+video, return list
		videolist=[]
		namelist=[]
		selector=etree.HTML(NHTML)
		for i in [2,4]:
			for j in range(1,11):
				video=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/div[1]/@data-mp4'%(i,j))
				if video:
					name=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[1]/a/text()'%(i,j))
					videolist.append(video)
					namelist.append(name)
		return zip(videolist,namelist)
	
	
	def getImage(self,NHTML):    #obtain all image, return list
		imagelist=[]
		namelist=[]
		selector=etree.HTML(NHTML)
		for i in [2,4]:
			for j in range(1,11):
				image=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/a/img/@data-original'%(i,j))
				if image:
					name=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/a/img/@title'%(i,j))
					imagelist.append(image)
					namelist.append(name)
		return zip(imagelist,namelist)
	
	

if __name__=='__main__':

	crawl=Crawler(url=' http://www.budejie.com/')
	urllist=crawl.getURL()
	for i in range(1):
		HTML=crawl.getHTML(urllist[i])
		vlist=crawl.getVideo(HTML)
		imglist=crawl.getImage(HTML)
		print imglist




		
		
		
		
		
		