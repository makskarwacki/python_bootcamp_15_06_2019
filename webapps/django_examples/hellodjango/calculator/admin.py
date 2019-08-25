from django.contrib import admin
from calculator.models import Calculation, Prioritet


# Register your models here.

@admin.register(Calculation)
class AdminCalculation(admin.ModelAdmin):
    list_display = ['id', 'x', 'y', 'operation', 'created']
    readonly_fields = ['created']
    list_filter = ['x']
    search_fields = ['operation']

@admin.register(Prioritet)
class AdminPrioritet(admin.ModelAdmin):
    pass