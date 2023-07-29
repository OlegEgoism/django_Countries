from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Person, Organization


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Кандидат"""
    list_display = '__str__', 'birthday', 'country', 'preview'
    readonly_fields = 'preview',

    def preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="80" height="80" />')
        else:
            return 'Нет фотографии'

    preview.short_description = 'Фотография'


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Организация"""
    list_display = 'name',
