from eshop_contact.models import ContactUs
from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin
from .models import ContactUs
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_filter = ['is_read']
    search_fields = ['subject', 'text']


admin.site.register(ContactUs, ContactAdmin) 

