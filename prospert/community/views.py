from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def communityPage(request):
	return render(request, 'community/communityPage.html')
