import json	
import bs4 as bs	
import requests	
import csv	
from datetime import datetime,timedelta	
import sys	
import os
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../'
sys.path.insert(0,path)
	
from database.dbase import Dbase	
from news.news_obj import News	

site = "kantipur"	

def scrape():	
        news_list= []
        day = datetime.today()	
        for _ in range(5):         	
                url = "https://www.kantipurdaily.com/news/"+str(day)[:10].replace('-','/')+"?json=true"	
                #print(url)	
                day = day - timedelta(days=1)	
                r = requests.get(url)	
                # print(r.text)	
                p = bs.BeautifulSoup(json.loads(r.text)["html"],"lxml")	
                posts = p.find_all("h2")	
                for titles in posts:	
                        data = titles.find("a")	
                        link=(data["href"])	
                        title=(data.text)	
                        title= ' '.join(title.split(','))	
                        db=Dbase()	
                        latest_news = db.get_latest_news(site)	
                        for data in latest_news:
                                if data[0] == link:
                                        print("Kantipur returned ")
                                        return news_list
		        #print(latest_news)	
                        a=News(title,link,site)	
                        print(a.title)
                        news_list.append(a)	
        return news_list

if __name__=="__main__":	
        scrape() 
