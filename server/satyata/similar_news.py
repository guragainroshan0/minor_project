from gensim.models import KeyedVectors
import sys
import os

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
                res.append(News(data[1],data[0],data[2]))
        return res

def similar_news(text, threshold=15):
    embeddings = np + '/embeddings'
    wv = KeyedVectors.load(embeddings)
    similar =[]
    scrape.scrape()
    dbase = Dbase()
    news_data = news(dbase.get_latest_news('annapurnapost',150))+news(dbase.get_latest_news('nagarik',150))+news(dbase.get_latest_news('kantipur',150))+news(dbase.get_latest_news('onlinekhabar',150))
    for data in news_data:
        distance = wv.wmdistance(tokenstem(text),tokenstem(str(data.title)))
        if distance<threshold:
            print(data,distance)
            if data not in similar:
                similar.append(data)
    return similar

