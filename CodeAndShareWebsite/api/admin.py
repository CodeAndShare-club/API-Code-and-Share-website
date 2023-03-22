from django.contrib import admin
from .models import Blog, Project, Event, Sponsor, Category
# Register your models here.
admin.site.register(Blog),
admin.site.register(Category),
admin.site.register(Project),
admin.site.register(Event),
admin.site.register(Sponsor),