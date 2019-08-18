from django.conf.urls import url
from .views import MyHouse, book

urlpatterns = [
    url(r'house', MyHouse.as_view()),
    url(r'book', book)
]