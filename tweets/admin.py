from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')  # Show these fields in the admin list view
    search_fields = ('content',)              # Enable search by tweet content
    list_filter = ('created_at',)             # Filter tweets by creation date
