from django.contrib import admin

from .models import Member, Event, Expenses

# Register your models here.
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Expenses)