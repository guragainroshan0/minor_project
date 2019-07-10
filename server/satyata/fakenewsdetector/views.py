from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request,news):

    response = find_similar(news)
    return HttpResponse(json.dumps(response))


def find_similar(news):
    return 'similar news to be checked','sadf'