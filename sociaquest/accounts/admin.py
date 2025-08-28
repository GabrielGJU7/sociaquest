from django.contrib import admin
from .models import Avatar

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ['user', 'nivel', 'xp', 'carisma', 'empatia']
    list_filter = ['nivel', 'estilo_avatar']
    search_fields = ['user__username']