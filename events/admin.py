from django.contrib import admin

from events.models import Event, EventType


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event_type', 'timestamp', 'created_at')
    list_filter = ('event_type', 'timestamp')


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
