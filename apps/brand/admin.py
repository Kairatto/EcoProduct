from django.contrib import admin
from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline')
    search_fields = ('title', 'tagline')
