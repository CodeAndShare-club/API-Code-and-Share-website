from django.urls import path, include
from rest_framework import routers
from .views import BlogViewSet, BlogImageViewSet, SponsorViewSet, EventViewSet, ProjectViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'blogimages', BlogImageViewSet, basename='blogimage')
router.register(r'sponsors', SponsorViewSet, basename='sponsor')
router.register(r'events', EventViewSet, basename='event')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
