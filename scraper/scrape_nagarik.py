import bs4 as bs
import requests
import sys
import os
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../'
sys.path.insert(0,path)

from database.dbase import Dbase
from news.news_obj import News
from time import time
url ="https://nagariknews.nagariknetwork.com"
site = "nagarik"


def getid(data):
        """Returns the id of latest news using url"""
        return int(data.split('/')[-2])

def scrape():
    """Scrapes the news"""
    db = Dbase()
    news_list = []
    
    #number of pages to be scraped when the system is run first time i.e database is empty
    page = 15
    for page_number in range(1,int(page)): 
        urls ='https://nagariknews.nagariknetwork.com/category/21?page='+str(page_number)
        #send request
        sauce = requests.get(urls)
        #get response
        soup = bs.BeautifulSoup(sauce.text,'lxml')
        #HTML response id different if page ==1 and same for all other pages
        if page_number == 1:
            data = soup.find_all("div",class_="col-sm-3 part-ent")
            for d in data:
                title = d.find('a').text
                link = url +d.find('a')['href']
                print(link)
                a = ins(title,link,db)
                if a.link()=='0':
                    print("Nagarik Returned")
                    return news_list
                news_list.append(a)
                
                
        else:
            posts = soup.find_all('div',class_="col-sm-9 detail-on")
            for data in posts:
                title = data.find('a').text
                link = url+data.find('a')['href']
                print(link)
                a = ins(title,link,db)
                if a.link()=='0':
                    print("Nagarik Returned")
                    return news_list
                news_list.append(a)
    return news_list

def ins(title,link,db,site="nagarik"):
        """Return only the news not in database"""
        news = News(title,link,site)
        latest_news = db.get_latest_news(site)
        for data in latest_news:
            print(getid(data[0]))
            if getid(data[0]) >= getid(link):
                #print("Nagarik Returned")
                return News('0','0','0') 
        return news


        


if __name__=="__main__":
    scrape()
