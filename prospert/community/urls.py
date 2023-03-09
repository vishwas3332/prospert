from django.urls import path
from . import views


urlpatterns = [
	path('',views.communityPage, name='CommunityPage'),
]