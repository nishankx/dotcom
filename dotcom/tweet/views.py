from django.shortcuts import render
from .models import Tweet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html',{'tweets': tweets})