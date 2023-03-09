from django.shortcuts import render

# Create your views here.

def stockPage(request):
	return render(request, 'Stocks/stocksPage.html')