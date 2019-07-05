import bs4 as bs
import requests
import sys
sys.path.insert(0,'../')
from news.news_obj import News
from database.dbase import Dbase

url ="https://nagariknews.nagariknetwork.com"
site = "nagarik"

def scrape():
    db = Dbase()
    #page = input('Page number each page contains 21 post')
    page = 10
    for page_number in range(1,int(page)): 
        sauce = requests.get('https://nagariknews.nagariknetwork.com/category/21?page='+str(page_number))
        soup = bs.BeautifulSoup(sauce.text,'lxml')
        if page_number == 1:
            data = soup.find_all("div",class_="col-sm-3 part-ent")
            for d in data:
                title = d.find('a').text
                link = url +d.find('a')['href']
                print(title+'\n'+link)
                a = ins(title,link,db)
                if a==0:
                    return
                
        else:
            print(page_number)
            posts = soup.find_all('div',class_="col-sm-9 detail-on")
            for data in posts:
                title = data.find('a').text
                link = url+data.find('a')['href']
                print(title+'\n'+link)
                a = ins(title,link,db)
                if a==0:
                    return

def ins(title,link,db,site="nagarik"):
        news = News(title,link,site)
        latest_news = db.get_latest_news(site)
        for data in latest_news:
            if data[0] == link:
                print("returned")
                return 0 
        db.insert_news(news)


        


if __name__=="__main__":
    scrape()
