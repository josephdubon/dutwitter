from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Tweet


# Home View
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home</h1>")


# Tweet Detail View
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>Home {tweet_id} - {obj.content} </h1>")
