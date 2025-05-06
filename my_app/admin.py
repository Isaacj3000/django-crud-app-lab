from django.contrib import admin
from .models import Plant, WateringRecord

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'watering_frequency', 'last_watered', 'created_at')
    list_filter = ('species', 'watering_frequency')
    search_fields = ('name', 'species', 'notes')
    ordering = ('name',)

@admin.register(WateringRecord)
class WateringRecordAdmin(admin.ModelAdmin):
    list_display = ('plant', 'watered_at', 'created_at')
    list_filter = ('plant', 'watered_at')
    search_fields = ('plant__name', 'notes')
    ordering = ('-watered_at',)
