import json
import bs4 as bs
import requests
import csv
from datetime import datetime,timedelta
import sys
sys.path.insert(0,'../')
from database.dbase import Dbase
from news.news_obj import News

site = "kantipur"

def scrape():
        day = datetime.today()
        for _ in range(20):         
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
                        a=News(title,link,site)
                        latest_news = db.get_latest_news(site)
		        #print(latest_news)
                        for data in latest_news:
                                if data[0] == link:
                                        exit
                        db.insert_news(a)

if __name__=="__main__":
        scrape()