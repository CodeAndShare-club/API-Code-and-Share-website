from .models import Blog, BlogImage, Sponsor, Event, Project
from rest_framework import serializers


#Blog

class BlogImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = BlogImage
        fields = "__all__"



class BlogSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = "__all__"


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