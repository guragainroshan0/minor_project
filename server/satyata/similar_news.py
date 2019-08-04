from gensim.models import KeyedVectors
from gensim.similarities import WmdSimilarity
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
        print("News function")
        for data in dt:
                res.append(News(data[1],data[0],data[2],data[3]))
        return res

def similar_news(text, threshold=15):
    print(text)
    #threshold=3.5
    embeddings = np + '/embeddings'
    wv = KeyedVectors.load(embeddings)
    dbase = Dbase()
    date = dbase.get_date()
    similar =[]
    
    num_of_news= 50
    news_data = news(dbase.get_latest_news('annapurnapost',num_of_news))+news(dbase.get_latest_news('nagarik',num_of_news))+news(dbase.get_latest_news('kantipur',num_of_news))+news(dbase.get_latest_news('onlinekhabar',num_of_news))
    for data in news_data:
        #distance = wv.wmdistance(text.spl#scrape.scrape()#scrape.scrape()#scrape.scrape()#scrape.scrape()#scrape.scrape()#scrape.scrape()it(' '),str(data.title).split(' '))
        distance = wv.wmdistance(tokenstem(text),tokenstem(str(data.title)))
        #print(distance)
        if distance<float(threshold):
            if data not in similar:
                print(data,distance)
                similar.append(data)


def simi_news(text, threshold=0.5,num_best=10):
    dbase = Dbase()
    date = dbase.get_date()
    embeddings = np + '/embeddings'
    wv = KeyedVectors.load(embeddings)
    date = dbase.get_date()
    for d in date:
        a  = d[0]
    if (a - datetime.datetime.now()) < datetime.timedelta(0,0,0,0,5,0,0):
        scrape.scrape()
#     scrape.scrape()
    similar =[]
    clean_data =[]
    num_of_news= 50
    news_data = news(dbase.get_latest_news('nagarik',num_of_news))+news(dbase.get_latest_news('kantipur',num_of_news))+news(dbase.get_latest_news('onlinekhabar',num_of_news))+news(dbase.get_latest_news('annapurnapost',num_of_news))
    for data in news_data:
        clean_data.append(tokenstem(data.title()))
    clean_news = tokenstem(text)
    #print(clean_data)
    instance = WmdSimilarity(clean_data,wv,num_best=10)
    result = instance[clean_news]  
    print(len(result)) 
    for offset,similarity in result:
            # print(result[i][1],news_data[i].title())
            # print(result[i][1])
            if similarity > threshold:
                #print(result[i][1],news_data[i].title())
                similar.append(news_data[offset])
        #     print(result[i][1],clean_data[i],news_data[i].title())
    # print(len(news_data))
    return similar

    