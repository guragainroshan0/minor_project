import requests
import json
import sys
sys.path.insert(0,'../')
from news.news_obj import News
from database.dbase import Dbase
from time import time

url = "http://annapurnapost.com/news/"
site="annapurnapost"

def scrape():
        news_list = []
        for i in range(0,5):
                resp = requests.get("http://bg.annapurnapost.com/api/news/list?page="+str(i)+"&per_page="+str(30)+"&category_alias=politics&isCategoryPage=1")
                p = json.loads(resp.text)
                data = p["data"]
                for post in data:
                        title = post["title"]
                        link = url+str(post["id"])
                        db = Dbase()
                        latest_news = db.get_latest_news(site)
                        for data in latest_news:
                                #print(data[0],link)
                                if data[0] == link:
                                        
                                        print("Annapurna post returned")
                                        return news_list
                        #print(len(news_list))
                        a = News(title,link,site)
                        news_list.append(a)
        return news_list
                        
if __name__=="__main__":
        scrape()
