from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from authentication.viewsets import UserViewSet
from home.views import NewsFeedViewSet,SermonsViewSet,SermonAttendanceViewSet,AnnouncementsViewSet,TestimoniesViewSet
from django.conf.urls.static import static 
from django.conf import settings as st

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'feeds', NewsFeedViewSet)
router.register(r'sermons', SermonsViewSet)
router.register(r'attendance', SermonAttendanceViewSet)
router.register(r'announcements', AnnouncementsViewSet)
router.register(r'testimonies', TestimoniesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('authentication/', include('authentication.urls'))
]

urlpatterns += static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)
urlpatterns += static(st.STATIC_URL, document_root=st.STATIC_ROOT)

