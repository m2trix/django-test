from django.contrib import admin
from .models import UrlHead, UrlBody

@admin.register(UrlHead)
class UrlHeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_env', 'url_domain', 'url_port', 'is_deleted')

@admin.register(UrlBody)
class UrlBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_name', 'url_path', 'url_params', 'is_deleted')