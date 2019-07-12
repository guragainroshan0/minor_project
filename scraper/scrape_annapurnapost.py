import requests
import json
import sys
import os
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../'
sys.path.insert(0,path)
from news.news_obj import News
from database.dbase import Dbase
from time import time

url = "http://annapurnapost.com/news/"
site="annapurnapost"

def getid(data):
        return int(data.split('/')[-1])

def scrape():
        news_list = []
        for i in range(0,5):
                urls= "http://bg.annapurnapost.com/api/news/list?page="+str(i)+"&per_page="+str(60)+"&category_alias=politics&isCategoryPage=1"
                print(urls)
                resp = requests.get(urls)
                p = json.loads(resp.text)
                data = p["data"]
                for post in data:
                        title = post["title"]
                        link = url+str(post["id"])
                        db = Dbase()
                        latest_news = db.get_latest_news(site)
                        for data in latest_news:
                                #print(data[0],link)
                                if getid(data[0]) >= post["id"]:
                                        print(data[0])
                                        print("Annapurna post returned")
                                        return news_list
                        #print(len(news_list))
                        a = News(title,link,site)
                        if a not in news_list:
                                news_list.append(a)
        return news_list
                        
if __name__=="__main__":
        scrape()
