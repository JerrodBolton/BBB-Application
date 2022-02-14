from django.contrib import admin
from BackEnd_For_BBB.BBBBackEnd.BBBapp.views import BBBList
from views import BBBList
from django.urls import path, include

urlpatterns = [    
    path('', BBBList.as_view(), name='post_list'),

]
