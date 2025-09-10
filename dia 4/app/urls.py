from django.urls import path
from .views import home,hello,listarpessoas,criarpessoas

urlpatterns = [
    path('',home, name='url_home'),
    path('hello/',hello, name='url_hello'),
    path('lista/',listarpessoas, name='url_listarpessoas'),
    path('criar/',criarpessoas, name='url_criar')
]