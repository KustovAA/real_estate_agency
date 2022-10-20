from django.contrib import admin

from .models import Flat, Complain, Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


class OwnerInline(admin.StackedInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    inlines = (OwnerInline,)
    raw_id_fields = ('liked_by',)


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
