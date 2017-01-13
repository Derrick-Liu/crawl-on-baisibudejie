#coding:utf-8
import requests
from lxml import etree
from Tkinter import *
from ScrolledText import ScrolledText   #文本滚动框
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Crawler:
	def __init__(self,url):
		self.rooturl=url
		self.id=1
		
		
	def createGUI(self):
		window=Tk()
		window.title('爬取百思不得姐')
		self.text=ScrolledText(window,width=80,height=20,font=('微软雅黑',10))
		self.text.grid()
		
		button1=Button(window,text='开始爬取视频',font=('微软雅黑',10),command=self.getVideo)
		button2=Button(window,text='开始爬取图片',font=('微软雅黑',10),command=self.getImage)
		button1.grid()
		button2.grid()
		
		self.var1=StringVar()
		label=Label(window,font=('微软雅黑',10),fg='red',textvariable=self.var1)
		label.grid()
		self.var1.set('爬取已经准备好...')

		window.mainloop()
		
	# def getURL(self):           #return list
		# urllist=[]
		# for i in range(1,51):
			# urllist.append(self.rooturl+str(i))
		# return urllist
	
	def getHTML(self,url):      #return html(str) of each page
		header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
		html=requests.get(url,headers=header).content
		return html
		
	def getVideo(self):    #obtain name+video, return list
		
		videolist=[]
		namelist=[]
		for num in range(1,10):
			self.var1.set('正在爬取第%s页视频...'%str(num))
			urlnow=self.rooturl+str(num)
			NHTML=self.getHTML(urlnow)
			selector=etree.HTML(NHTML)
			for i in [2,4]:
				for j in range(1,11):
					video=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/div[1]/@data-mp4'%(i,j))
					if video:
						name=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[1]/a/text()'%(i,j))
						videolist.append(video)
						namelist.append(name)
						self.text.insert(END,str(self.id)+'.'+video[0]+'\n'+name[0]+'\n\n')
						self.id+=1
		return zip(videolist,namelist)
	
	
	def getImage(self):    #obtain all image, return list
		id=1
		imagelist=[]
		namelist=[]
		for num in range(1,10):
			self.var1.set('正在爬取第%s页图片...'%str(num))
			urlnow=self.rooturl+str(num)
			NHTML=self.getHTML(urlnow)
			selector=etree.HTML(NHTML)
			for i in [2,4]:
				for j in range(1,11):
					image=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/a/img/@data-original'%(i,j))
					if image:
						name=selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div[%d]/ul/li[%d]/div[2]/div[2]/a/img/@title'%(i,j))
						imagelist.append(image)
						namelist.append(name)
						self.text.insert(END,str(self.id)+'.'+image[0]+'\n'+name[0]+'\n\n')
						self.id+=1
		return zip(imagelist,namelist)
	
	

if __name__=='__main__':
	
	crawl=Crawler(url=' http://www.budejie.com/')
	# urllist=crawl.getURL()
	# for i in range(2):
		# HTML=crawl.getHTML(urllist[i])
		# var1.set('正在爬取第%s页视频...'%str(i+1))
		# vlist=crawl.getVideo(HTML)
		# print vlist
		# var1.set('正在爬取第%s页图片...'%str(i+1))
		# imglist=crawl.getImage(HTML)
		# print imglist
	# var1.set('网站信息已爬取完毕...')
	crawl.createGUI()
		
		



		
		
		
		
		
		