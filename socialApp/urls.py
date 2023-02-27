from django.urls import path
from .views import Booklist

urlpatterns = [
    path('', Booklist.as_view() , name='books')
]
