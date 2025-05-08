from django.contrib import admin
from .models import Service, Project, Testimonial, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title', 'description')
    
    def short_description(self, obj):
        """Return a truncated description for the list view"""
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    
    short_description.short_description = 'Description'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed', 'short_description')
    list_filter = ('date_completed',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date_completed'
    
    def short_description(self, obj):
        """Return a truncated description for the list view"""
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    
    short_description.short_description = 'Description'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'short_quote')
    list_filter = ('location',)
    search_fields = ('name', 'location', 'quote')
    
    def short_quote(self, obj):
        """Return a truncated quote for the list view"""
        return obj.quote[:100] + '...' if len(obj.quote) > 100 else obj.quote
    
    short_quote.short_description = 'Quote'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date_sent', 'short_message')
    list_filter = ('date_sent',)
    search_fields = ('first_name', 'last_name', 'email', 'message')
    readonly_fields = ('date_sent',)
    
    def full_name(self, obj):
        """Return the full name of the contact"""
        return f"{obj.first_name} {obj.last_name}"
    
    def short_message(self, obj):
        """Return a truncated message for the list view"""
        return obj.message[:100] + '...' if len(obj.message) > 100 else obj.message
    
    full_name.short_description = 'Name'
    short_message.short_description = 'Message'