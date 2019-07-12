from bs4 import BeautifulSoup as soup
import requests
import sys
import os
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../'
sys.path.insert(0,path)

from database.dbase import Dbase
from news.news_obj import News

site="onlinekhabar"
def getid(data):
        return int(data.split('/')[-1])
def scrape():
	news_list = []
	for i in range(1,5):
		
		my_url ="https://www.onlinekhabar.com/content/news/page/"+str(i)

		r=requests.get(my_url)

		page_soup= soup (r.text,"lxml")

		containers= page_soup.findAll("div", {"class":"item__wrap"})
		for data in containers: 
			link=data.a['href']
			title=data.a.text.replace('\n','')
			title=' '.join(title.split(','))
			db = Dbase()
			latest_news = db.get_latest_news(site)
			#print(latest_news)
			for data in latest_news:
				if getid(data[0]) >= getid(link):
					print("Online Khabar Returned")
					return news_list
			a= News(title, link, site)
			if a not in news_list:     
				news_list.append(a)
		
	return news_list

if __name__ == "__main__":
	scrape()