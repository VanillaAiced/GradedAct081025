from django.urls import path
from tweets import views

urlpatterns = [
    path('', views.tweet_list_create, name='tweet_list_create'),
]