from bs4 import BeautifulSoup as soup
import requests
import sys
sys.path.insert(0,'../')
from database.dbase import Dbase
from news.news_obj import News

site="onlinekhabar"

for i in range(1,20):
	my_url ="https://www.onlinekhabar.com/content/news/page"+str(i)

	r=requests.get(my_url)

	page_soup= soup (r.text,"lxml")

	containers= page_soup.findAll("div", {"class":"item__wrap"})

	for data in containers: 
		link=data.a['href']
		title=data.a.text.replace('\n','')
		title=' '.join(title.split(','))
		db = Dbase()
		a= News(title, link, site)
		latest_news = db.get_latest_news(site)
		#print(latest_news)
		for data in latest_news:
			if data[0] == link:
				exit
		db.insert_news(a)