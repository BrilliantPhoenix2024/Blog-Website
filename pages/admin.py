from django.contrib import admin
from .models import My_design, Contact


@admin.register(My_design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', )
    ordering = ('-status', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'msg', )


# admin.site.register(My_design, My_designAdmin)

