from django.contrib import admin

from .models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_name', 'channel_img', 'channel_description', 'channel_url', 'channel_stat', 'channel_err', 'channel_crm',
                    'channel_coverage']
    list_filter = ['channel_category']
    search_fields = ['channel_name__startswith']
