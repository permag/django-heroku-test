from django.contrib import admin
from myproject.apps.myapp.models import Poll

class PollAdmin(admin.ModelAdmin):
    pass

admin.site.register(Poll, PollAdmin)