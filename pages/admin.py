from django.contrib import admin
from .models import My_design

@admin.register(My_design)
class My_designAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', )
    ordering = ('-status', )


# admin.site.register(My_design, My_designAdmin)

