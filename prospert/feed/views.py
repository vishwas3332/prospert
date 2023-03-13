from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def feedPage(request):
	feedApi = NewsApiClient(api_key='37c69975025a4cec803e6aafbb03fe5a')
	headlines = feedApi.get_top_headlines(category='business',country='in')
	articles = headlines['articles']
	context = {'articles':articles}
	return render(request, 'feed/feedPage.html',context)