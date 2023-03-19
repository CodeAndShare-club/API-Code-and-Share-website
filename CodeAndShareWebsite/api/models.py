# Create your models here.
from django.db import models



class Blog(models.Model):
    title= models.CharField(max_length=50)
    author= models.CharField(max_length=50)
    publish_date= models.DateField(auto_now_add=True)
    body= models.TextField()
    header= models.TextField()

    class Meta:
        ordering = ['-publish_date']


class BlogImage(models.Model):
    image= models.ImageField(upload_to='blogs/', editable=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='images')

class Event(models.Model):  
    name = models.CharField(max_length=15)
    description= models.TextField(blank=True)
    launch_date= models.DateField()
    icon = models.ImageField(upload_to='events/', editable=True)

class Project(models.Model):  
    name = models.CharField(max_length=15)
    description= models.TextField(blank=True)
    launch_date= models.DateField()
    photo = models.ImageField(upload_to='projects/', editable=True)

class Sponsor(models.Model):  
    name = models.CharField(max_length=15)
    description= models.TextField(blank=True)
    icon = models.ImageField(upload_to='sponsors/', editable=True)
