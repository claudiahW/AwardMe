


from django.contrib import admin
from django.urls import path,include
from weaward import views 

urlpatterns = [
    path('',views.index,name= 'index'),
    path('accounts/profile/', views.user_profile,name='profile'),
    path('post/project', views.post, name = "post"),
]
