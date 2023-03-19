from django.contrib import admin
from .models import Blog, BlogImage, Project, Event, Sponsor
# Register your models here.
admin.site.register(Blog),
admin.site.register(BlogImage),
admin.site.register(Project),
admin.site.register(Event),
admin.site.register(Sponsor),