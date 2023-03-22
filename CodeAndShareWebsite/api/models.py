# Create your models here.
from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    title= models.CharField(max_length=50)
    author= models.CharField(max_length=50)
    publish_date= models.DateField(auto_now_add=True)
    body=HTMLField()
    header= models.TextField()
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class Event(models.Model):  
    name = models.CharField(max_length=15)
    description= models.TextField(blank=True)
    launch_date= models.DateField()
    icon = models.ImageField(upload_to='events/', editable=True)

class Project(models.Model):  
    name = models.CharField(max_length=15)
    description= models.TextField(blank=True)
    launch_date= models.DateField()
    icon = models.ImageField(upload_to='projects/', editable=True)

class Sponsor(models.Model):  
    name = models.CharField(max_length=15)
    description= models.TextField(blank=True)
    icon = models.ImageField(upload_to='sponsors/', editable=True)
