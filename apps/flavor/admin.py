from django.contrib import admin
from .models import Flavor


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
