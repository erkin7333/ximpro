from django.contrib import admin
from .models import Blog, Location
from parler.admin import TranslatableAdmin



@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'loc')
    list_display_links = ('id', 'loc')
    class Meta:
        model = Location
admin.site.register(Location, LocationAdmin)