from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import *

# ViewSets define the view behavior.

# # # # # # # # # # # # # # # # # # NewsFeed # # # # # # # # # # # # # # # # # #


class NewsFeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsFeeds
        fields = ['picture', 'body', 'author', 'likes']

class NewsFeedViewSet(viewsets.ModelViewSet):
    queryset = NewsFeeds.objects.all()
    serializer_class = NewsFeedSerializer

# # # # # # # # # # # # # # # # # # EndNewsFeed # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # Sermons # # # # # # # # # # # # # # # # # #

class SermonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sermons
        fields = ['name', 'title', 'description', 'video', 'image']

# ViewSets define the view behavior.
class SermonsViewSet(viewsets.ModelViewSet):
    queryset = Sermons.objects.all()
    serializer_class = SermonsSerializer

# # # # # # # # # # # # # # # # # # Sermons # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # Attendance # # # # # # # # # # # # # # # # # #
class SermonAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SermonAttendance
        fields = ['male', 'female', 'children', 'count_by']

# ViewSets define the view behavior.
class SermonAttendanceViewSet(viewsets.ModelViewSet):
    queryset = SermonAttendance.objects.all()
    serializer_class = SermonAttendanceSerializer



# # # # # # # # # # # # # # # # # # Attendance # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # Announcements # # # # # # # # # # # # # # # # # #
class AnnouncementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcements
        fields = ['title', 'description', 'verse']

# ViewSets define the view behavior.
class AnnouncementsViewSet(viewsets.ModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer


# # # # # # # # # # # # # # # # # # EndAnnouncements # # # # # # # # # # # # # # # # # #

class TestimoniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testimonies
        fields = ['name', 'testimony']

# ViewSets define the view behavior.
class TestimoniesViewSet(viewsets.ModelViewSet):
    queryset = Testimonies.objects.all()
    serializer_class = TestimoniesSerializer


