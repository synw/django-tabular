# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'updated',
        'modelnames',
        'generator',
    )
    list_filter = ('updated',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ("updated",)
