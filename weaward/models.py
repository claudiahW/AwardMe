from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
'''
create models class
'''


class Profile(models.Model):
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile/')
  bio = models.TextField()
  contact=models.CharField(max_length=100)
  user = models.OneToOneField(User,on_delete = models.CASCADE)

def save_profile(self):
    self.save()

def delete_profile(self):
     self.save()

def update_profile(self):
     self.save() 

@classmethod
def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

def _str_(self):
        return self.user.username
         
'''
Create project class

'''

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = CloudinaryField("image")
    url = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    # update project
    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def _str_(self):
        return self.title