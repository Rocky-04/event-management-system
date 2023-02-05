import json

from rest_framework import serializers

from .models import Event, EventType


class EventTypeSerializer(serializers.ModelSerializer):
    """Serializer for the EventType model"""

    class Meta:
        model = EventType
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model"""

    class Meta:
        model = Event
        fields = '__all__'

    def validate_info(self, value):
        """
        Validate the 'info' field to ensure it is in a valid JSON format
        """
        try:
            json.loads(value)
        except ValueError:
            raise serializers.ValidationError("Invalid JSON format")
        return value
