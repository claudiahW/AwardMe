


from django.contrib import admin
from django.urls import path,include
from weaward import views 

urlpatterns = [
    path('',views.index,name= 'index'),
]
