from django.contrib import admin

from .models import Flat, Complain


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building',)


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)