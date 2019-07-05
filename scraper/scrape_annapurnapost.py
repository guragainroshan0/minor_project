import requests
import json
import sys
sys.path.insert(0,'../')
from news.news_obj import News
from database.dbase import Dbase

url = "http://annapurnapost.com/news/"
site="annapurnapost"

def scrape():
        for i in range(0,5):
                resp = requests.get("http://bg.annapurnapost.com/api/news/list?page="+str(i)+"&per_page="+str(30)+"&category_alias=politics&isCategoryPage=1")
                p = json.loads(resp.text)
                data = p["data"]
                for post in data:
                        title = post["title"]
                        link = url+str(post["id"])
                        print(title)
                        a = News(title,link,site)
                        db = Dbase()
                        latest_news = db.get_latest_news(site)
                        for data in latest_news:
                                if data[0] == link:
                                        return
                        db.insert_news(a)
if __name__=="__main__":
        scrape()
