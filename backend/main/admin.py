from django.contrib import admin

from .models import Player, Team


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Player', {
            'fields': (('name', 'last_name'), 'nationality')
        }),
        ('Club', {
            'fields': ('team', 'position')
        })
    )

    list_display = ('id', 'name', 'last_name', 'nationality', 'team', 'position')
    list_editable = ('name', 'last_name', 'nationality', 'team', 'position')
    list_filter = ('team', 'position')
    search_fields = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Team', {
            'fields': ('name',)
        }),
    )

    list_display = ('id', 'name')
    list_editable = ('name', )
