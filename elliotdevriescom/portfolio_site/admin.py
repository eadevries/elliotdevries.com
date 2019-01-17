from django.contrib import admin

from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'body_preview',
                    'sent_date', 'urgency', 'handled')
    list_filter = ['sent_date', 'handled', 'urgency']
    search_fields = ['name', 'organization', 'subject', 'email', 'body']


admin.site.register(ContactMessage, ContactMessageAdmin)
