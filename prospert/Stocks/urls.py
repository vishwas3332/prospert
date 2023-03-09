from django.urls import path
from . import views


urlpatterns = [
	path('', views.stockPage, name='StockPage'),
]