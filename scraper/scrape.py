
from multiprocessing import Process,current_process,pool
import sys
import os
path = os.path.abspath(__file__).split('/')[:-1]
sys.path.insert(0,'/'.join(path))
path = '/'.join(path)+'/../'
sys.path.insert(0,path)
import scrape_kantipur
import scrape_nagarik
import scrape_onlinekhabar
import scrape_annapurnapost
from database.dbase import Dbase
from datetime import datetime



def insert_news(news):

    """ Inserts scraped news to database """
    db = Dbase()
    d = datetime.now()
    news.set_date(d)
    #print(news.title(),news.site())
    db.insert_news(news)

    
def scrape():

    """Scraped all the news from various sites """
    news_list = []
    processes = []

    news_list = news_list + scrape_nagarik.scrape()
    news_list = news_list + scrape_annapurnapost.scrape("politics")
    news_list = news_list + scrape_kantipur.scrape('news')
    news_list = news_list + scrape_kantipur.scrape("national")
    news_list = news_list + scrape_onlinekhabar.scrape()

    news_list = news_list[::-1]
    for news in news_list:
        process = Process(target=insert_news,args=(news,))
        processes.append(process)
        process.start()
if __name__ == "__main__":
        scrape()