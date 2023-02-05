from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import EventType
from .serializers import EventSerializer
from .serializers import EventTypeSerializer


class EventViewSet(generics.CreateAPIView):
    """ViewSet for handling the creation of events"""
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates an event instance in the database.
        If the provided event type name does not exist, it creates a new event type instance.
        """

        event_type_name = request.data['event_type']
        event_type = EventType.objects.filter(name=event_type_name).first()
        if not event_type:
            event_type_serializer = EventTypeSerializer(data={'name': event_type_name})
            event_type_serializer.is_valid(raise_exception=True)
            event_type = event_type_serializer.save()

        data = {
            'info': request.data.get('info'),
            'timestamp': request.data.get('timestamp'),
            'user': request.user.pk,
            'event_type': event_type.pk
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
