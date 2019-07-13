from gensim.models import KeyedVectors
import sys
import os
import datetime

path = os.path.abspath(__file__).split('/')[:-1]
np = '/'.join(path)
sys.path.insert(0,np)
from np_lang.tokenize.tokenizer import Tokenizer
from np_lang.stem.itrstem import IterativeStemmer
path = '/'.join(path)+'/../../'
sys.path.insert(0,path)

from nltk.corpus import stopwords
print(os.path.dirname(__file__))
from news.news_obj import News
from database.dbase import Dbase
from scraper import scrape


def tokenstem(data):
    nepali_sw = stopwords.words("nepali")
    a = Tokenizer()
    s = IterativeStemmer()
    return [s.stem(data) for data in a.word_tokenize(data) if data not in nepali_sw]

def news(dt):
        res = []
        for data in dt:
                res.append(News(data[1],data[0],data[2],data[3]))
        return res

def similar_news(text, threshold=15):
    print(text)
    embeddings = np + '/embeddings'
    wv = KeyedVectors.load(embeddings)
    dbase = Dbase()
    date = dbase.get_date()
    similar =[]
    for d in date:
        a  = d[0]
    if a - datetime.datetime.now() > datetime.timedelta(0,0,0,0,5,0,0):
        scrape.scrape()
    news_data = news(dbase.get_latest_news('annapurnapost',150))+news(dbase.get_latest_news('nagarik',150))+news(dbase.get_latest_news('kantipur',150))+news(dbase.get_latest_news('onlinekhabar',150))
    for data in news_data:
        #distance = wv.wmdistance(text.split(' '),str(data.title).split(' '))
        distance = wv.wmdistance(tokenstem(text),tokenstem(str(data.title)))
        if distance<threshold:
            if data not in similar:
                print(data,distance)
                similar.append(data)

    return similar

