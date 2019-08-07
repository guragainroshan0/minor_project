from gensim.models import KeyedVectors , FastText
# from gensim.models.wrappers import FastText
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
    """
    Removes the stop words, tokenize  and stem the text
    """
    nepali_sw = stopwords.words("nepali")
    a = Tokenizer()
    s = IterativeStemmer()
    return [s.stem(data) for data in a.word_tokenize(data) if data not in nepali_sw]

def news(dt):
        """
        Takes the database query result and converts into news object
        """
        res = []
        print("News function")
        for data in dt:
                res.append(News(data[1],data[0],data[2],data[3]))
        return res

# def similar_news(text, threshold=15):
#     print(text)
#     #threshold=3.5
#     embeddings = np + '/embeddings'
#     wv = KeyedVectors.load(embeddings)
#     dbase = Dbase()
#     date = dbase.get_date()
#     similar =[]
    
#     num_of_news= 50
#     news_data = news(dbase.get_latest_news('annapurnapost',num_of_news))+news(dbase.get_latest_news('nagarik',num_of_news))+news(dbase.get_latest_news('kantipur',num_of_news))+news(dbase.get_latest_news('onlinekhabar',num_of_news))
#     for data in news_data:
#         #distance = wv.wmdistance(text.spl#scrape.scrape()#scrape.scrape()#scrape.scrape()#scrape.scrape()#scrape.scrape()#scrape.scrape()it(' '),str(data.title).split(' '))
#         distance = wv.wmdistance(tokenstem(text),tokenstem(str(data.title)))
#         #print(distance)
#         if distance<float(threshold):
#             if data not in similar:
#                 print(data,distance)
#                 similar.append(data)


def simi_news(text, threshold=0.56,num=5):
    """
        Calculate similarity of between text and data in database
        text: input text
        threshold : degree of similarity between input text and text in database
        num : top results of similarity
    """    

    
    #load embedding vector
    embeddings = np + '/fasttext'
    wv = FastText.load(embeddings)
    
    #initialize database for getting date of when the data was last scraped
    dbase = Dbase()
    date = dbase.get_date()
    for d in date:
        a  = d[0]

    # if the time now and latest scrape time is greater than 5 scrape again    
    if (datetime.datetime.now()- a ) > datetime.timedelta(0,0,0,0,5,0,0):
        print("DELTA",datetime.datetime.now()- a )
        print(a)
        scrape.scrape()


    similar =[]
    all_data = []
    clean_data =[]

    # number of news to extract from database used to query database
    num_of_news= 50
    news_data = news(dbase.get_latest_news('nagarik',limit=num_of_news))+news(dbase.get_latest_news('kantipur',limit=num_of_news))+news(dbase.get_latest_news('onlinekhabar',limit=num_of_news))+news(dbase.get_latest_news('annapurnapost',limit=num_of_news))
   
    
    # if the news in database is older than 4 days then ignore the news
    for data in news_data:
        if (datetime.datetime.now()-data.date()) < datetime.timedelta(4,0,0,0,0,0,0):
                clean_data.append(tokenstem(data.title()))
                all_data.append(data)

    #sanitize the input text
    clean_news = tokenstem(text)
    
    
    """
    Provides the similarity of news from the clean data from database
    clean_data : data from database i.e title
    wv : word vector model
    num : number of best data to get
    """
    instance = WmdSimilarity(clean_data,wv,num_best=num)

    """ 
    result is the list of tuple of similarity 
    and the offset of the similar news offset is used
    to get data in all data variable 
     """
    result = instance[clean_news]  
    for offset,similarity in result:
            print(news,all_data[offset],similarity)
            if similarity > threshold:
                similar.append(all_data[offset])
    return similar

    