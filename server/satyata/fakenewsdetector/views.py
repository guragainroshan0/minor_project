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
def index(request,news):
    response = find_similar(news)
    response = {"result":response,"news":news}
    #return render(request,'fakenewsdetector/a.html',response)
    return HttpResponse(json.dumps(response))


def find_similar(news):
    res = []
    result = similar_news.simi_news(news)
    for data in result:
        #print(data.title())
        response = {
            "title":data.title(),
            "link":data.link(),
            "site":data.site()
            
        }
        if response not in res:
            res.append(response)
    return res