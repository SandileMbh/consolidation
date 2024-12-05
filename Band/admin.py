from django.contrib import admin
from .models import Event

"""
Admin configuration for the band website.
Registers the Event model in the Django admin site to allow
administrators to create, edit, and delete events from the admin interface."""
admin.site.register(Event)
