from sqlalchemy import create_engine
from datetime import datetime
import sys
import os
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../'
sys.path.insert(0,path)

from news.news_obj import News

class Dbase:
    def __init__(self):
        self._engine = create_engine("mysql+pymysql://roshan:EnterPassword@localhost/satyata?host=localhost?port=3306")
        self._conn = self._engine.connect()
#result = conn.execute("Insert into news values (2,'roshan','rosan','sadfsadf','2015-11-05 14:29:36')")

    def insert_news(self, news):
        #query = "INSERT INTO news(title,site,link,date) values ('{}','{}','{}','{}')".format(str(news.title()),str(news.site()),str(news.link()),datetime.now())
        query = 'INSERT INTO news (title,site,link,date) VALUES (%s,%s,%s,%s)'
        self._conn.execute(query,news.title(),news.site(),news.link(),datetime.now())

    def execute(self,query):
        self._conn.execute(query)

    def get_latest_news(self,site,limit=1):
        query = "SELECT link,title,site FROM news WHERE site='{}' order by link DESC LIMIT {}".format(site,limit)
        result = self._conn.execute(query)
        return result

    def get_news(self):
        a = self._conn.execute("Select * from news")
        for data in a:
            print(data)
