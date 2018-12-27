from django.urls import path
from django.conf.urls import url
from books import views


urlpatterns = [
    url(r'^books/$', views.BookListInfo.as_view(), name='booklist')
]
