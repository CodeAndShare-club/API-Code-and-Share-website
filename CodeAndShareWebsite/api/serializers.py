from .models import Blog, Sponsor, Event, Project, Category
from rest_framework import serializers


#Blog
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Category
        fields = "__all__"



class BlogSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    categories= serializers.StringRelatedField(many=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'publish_date', 'header', 'body', 'categories']


#Sponsor
class SponsorSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Sponsor
        fields = "__all__"


#Project
class ProjectSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = "__all__"

#Event
class EventSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = "__all__"