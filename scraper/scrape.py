import scrape_kantipur
import scrape_nagarik
import scrape_onlinekhabar
import scrape_annapurnapost
from multiprocessing import Process,current_process,pool
import sys
sys.path.insert(0,'../')
from database.dbase import Dbase
from time import time


t1 = time()
def insert_news(news):
    db = Dbase()
    #print(news.title(),news.site())
    db.insert_news(news)

news_list = []
processes = []

news_list = news_list + scrape_nagarik.scrape()
news_list = news_list + scrape_annapurnapost.scrape()
news_list = news_list + scrape_kantipur.scrape()
news_list = news_list + scrape_onlinekhabar.scrape()

news_list = news_list[::-1]
for news in news_list:
    process = Process(target=insert_news,args=(news,))
    processes.append(process)
    process.start()

print(time()-t1)