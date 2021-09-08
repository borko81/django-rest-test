from django.contrib import admin

from .models import Poll, Choices, Vote

admin.site.register(Poll)
admin.site.register(Choices)
admin.site.register(Vote)
