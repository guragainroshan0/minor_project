import pandas as pd
import nltk
from nltk.corpus import stopwords
import gensim
from np_lang.tokenize.tokenizer import Tokenizer
from np_lang.stem.itrstem import IterativeStemmer
from gensim import corpora, models ,similarities
from time import time

t1 = time()
def tokenstem(data):
    a = Tokenizer()
    s = IterativeStemmer()
    return [s.stem(data) for data in a.word_tokenize(data)]

#stopwords from nltk.corpus
nep_stopwords = stopwords.words("nepali")
#use iterative stemmer from np_lang
stemmer = IterativeStemmer()

#get data from csv files and remove empty rows
df = pd.read_csv("allnews.csv").dropna()
df1 = pd.read_csv("goodNewsData").dropna()
df2 = pd.read_csv("data.csv").dropna()
df3 = pd.read_csv("Nepali_News_Classification.csv").dropna()

#retrieve specific column in csv file
news = df['news'].values.tolist()
news = news + df1['noStopWords'].values.tolist() 
news = news+ df2['News article'].values.tolist()
news = news + df3['paras'].values.tolist()

good_corpus = []

for data in news:
    good_corpus.append(tokenstem(data))
print(good_corpus[:2])
model = models.Word2Vec(good_corpus,min_count=100,size=200,workers=15)
model.wv.save("embeddings")
print(time()-t1)