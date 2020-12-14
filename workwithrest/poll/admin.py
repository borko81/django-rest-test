from django.contrib import admin

from .models import *


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_by', 'pub_date')
    list_filter = ('question',)

    class Meta:
        ordering = ('pub_date',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    # poll, choice_text
    list_display = ('choice', 'poll', 'voted_by')
    list_filter = ('poll',)

    class Meta:
        ordering = ('-pk', )


@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    list_display = ('poll', 'choice_text')

    class Meta:
        ordering = ('-pk')



