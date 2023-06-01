from django.urls import path
from first2.views import* 
app_name='first2'
urlpatterns =[
    path('generic/',generic,name='generic')
]