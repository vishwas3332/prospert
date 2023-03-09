from django.shortcuts import render

# Create your views here.

def feedPage(request):
	return render(request, 'feed/feedPage.html')