from django.urls import path

from events.views import EventViewSet

urlpatterns = [
    path('api/create', EventViewSet.as_view(), name='create'),
]
