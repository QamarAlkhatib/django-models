from django.contrib import admin
from .models import SnackModel

@admin.register(SnackModel)
class AdminThing(admin.ModelAdmin):
    list_display= ['name', 'purchaser', 'description']
    search_fields = ['name']
    list_display_links = ('purchaser',)
    list_display_description = ('description')

# admin.site.register(SnackModel)
