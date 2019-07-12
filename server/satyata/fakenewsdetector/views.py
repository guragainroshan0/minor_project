from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
path = os.path.abspath(__file__).split('/')[:-1]
path = '/'.join(path)+'/../../../'
sys.path.insert(0,path)
import similar_news
from news.news_obj import News
import json
# Create your views here.
def index(request,news,threshold):
    response = find_similar(news,threshold)
    return HttpResponse(json.dumps(response))


def find_similar(news,threshold):
    res = []
    result = similar_news.similar_news(news,threshold)
    for data in result:
        #print(data.title())
        response = {
            "title":data.title(),
            "link":data.link()
        }
        if response not in res:
            res.append(response)
    return res