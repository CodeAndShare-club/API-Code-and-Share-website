from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Blog, Category, Project, Sponsor, Event
from .serializers import CategorySerializer, BlogSerializer, EventSerializer, ProjectSerializer, SponsorSerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Categorys.
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    

class BlogViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Blogs.
    """
    def list(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Blog.objects.all()
        blog = get_object_or_404(queryset, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    

class BlogImageViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving BlogImages.
    """
    def list(self, request):
        queryset = BlogImage.objects.all()
        serializer = BlogImageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BlogImage.objects.all()
        blogImage = get_object_or_404(queryset, pk=pk)
        serializer = BlogImageSerializer(blogImage)
        return Response(serializer.data)
    

class SponsorViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Sponsors.
    """
    def list(self, request):
        queryset = Sponsor.objects.all()
        serializer = SponsorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sponsor.objects.all()
        sponsor = get_object_or_404(queryset, pk=pk)
        serializer = SponsorSerializer(sponsor)
        return Response(serializer.data)
    
class EventViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Events.
    """
    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    

class ProjectViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Projects.
    """
    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    

