from django.contrib import admin
from django.urls import path,include
from weaward import views
 

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile,name='profile'),
    path('post/project/', views.post, name = "post"),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('search/', views.search_project, name='search.post'),
    path("project/<int:project_id>/", views.project_details, name="project_details"),
    path('rate/<int:id>',views.rate, name='rate'),
    # path('api/projects/', views.ProjectList.as_view()),
    # path('api/profiles/',views.ProfileList.as_view()),
]
