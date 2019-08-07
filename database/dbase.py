from sqlalchemy import create_engine
from datetime import datetime
import sys
import os
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../'
sys.path.insert(0,path)

from news.news_obj import News

class Dbase:
    """
    Database class handles all the database functions. 
    Sql alchemy is used to query database.
    """



    def __init__(self):

        """
        Initiates connection to mysql server
        """

        self._engine = create_engine("mysql+pymysql://roshan:EnterPassword@localhost/satyata?host=localhost?port=3306")
        self._conn = self._engine.connect()



    def insert_news(self, news):

        """
        Insert scraped news to database
        """
        
        query = 'INSERT INTO news (title,site,link,date) VALUES (%s,%s,%s,%s)'
        self._conn.execute(query,news.title(),news.site(),news.link(),news.date())

    def execute(self,query):
        self._conn.execute(query)

    def get_latest_news(self,site,type="",limit=1):

        """
        Returns the latest news in database in order of date in descending order
        site : site whose latest news is required
        type : type of news to be queried to database
        limit : number of news to be returnes
        """

        if type != "":
            query = 'SELECT link,title,site,date FROM news WHERE link like %s and site=%s order by link DESC LIMIT %s'
            data = ('%{}%'.format(type),site,limit)
            # print(query)
        else :
            query = "SELECT link,title,site,date FROM news WHERE site=%s order by link DESC LIMIT %s"
            data = (site,limit)
        result = self._conn.execute(query,data)
        return result

    def get_news(self):

        """
        Returns all news from database
        
        """

        a = self._conn.execute("Select * from news")
        for data in a:
            print(data)
    
    def get_date(self):

        """
        Returns the latest scraped date and time
        """
        
        return self._conn.execute("select date from news order by date desc limit 1")

