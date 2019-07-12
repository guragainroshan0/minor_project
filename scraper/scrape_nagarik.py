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
        return int(data.split('/')[-2])

def scrape():
    #t1 = time()
    db = Dbase()
    news_list = []
    #page = input('Page number each page contains 21 post')
    page = 15
    for page_number in range(1,int(page)): 
        urls ='https://nagariknews.nagariknetwork.com/category/21?page='+str(page_number)
        sauce = requests.get(urls)
        soup = bs.BeautifulSoup(sauce.text,'lxml')
        if page_number == 1:
            data = soup.find_all("div",class_="col-sm-3 part-ent")
            for d in data:
                title = d.find('a').text
                link = url +d.find('a')['href']
                print(link)
                a = ins(title,link,db)
                if a==0:
                    #print(time()-t1)
                    print("Nagarik Returned")
                    return news_list
                #print(len(news_list))
                news_list.append(a)
                #print(title+'\n'+link)
                
        else:
            #print(page_number)
            posts = soup.find_all('div',class_="col-sm-9 detail-on")
            for data in posts:
                title = data.find('a').text
                link = url+data.find('a')['href']
                print(link)
                a = ins(title,link,db)
                if a==0:
                    #print(time.now()-t1)
                    print("Nagarik Returned")
                    return news_list
                #print(len(news_list))
                news_list.append(a)
                #print(title+'\n'+link)
    #print(time.now()-t1)
    return news_list

def ins(title,link,db,site="nagarik"):
        news = News(title,link,site)
        latest_news = db.get_latest_news(site)
        for data in latest_news:
            print(getid(data[0]))
            if getid(data[0]) >= getid(link):
                #print("Nagarik Returned")
                return 0 
        return news


        


if __name__=="__main__":
    scrape()
