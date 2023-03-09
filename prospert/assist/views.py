from django.shortcuts import render

# Create your views here.

def assistPage(request):
	return render(request, 'assist/assistPage.html')