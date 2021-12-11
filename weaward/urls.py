


from django.contrib import admin
from django.urls import path,include
from weaward import views
 

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile,name='profile'),
    path('post/project/', views.post, name = "post"),
    path('update_profile/',views.update_profile, name='update_profile'),
]
