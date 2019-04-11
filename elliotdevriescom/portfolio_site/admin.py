from django.contrib import admin

from .models import ContactMessage, Project


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'body_preview',
                    'sent_date', 'urgency', 'handled')
    list_filter = ['sent_date', 'handled', 'urgency']
    search_fields = ['name', 'organization', 'subject', 'email', 'body']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'slug', 'blurb')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Project, ProjectAdmin)
