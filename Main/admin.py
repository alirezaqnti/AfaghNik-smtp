from django.contrib import admin

from .models import EmailTable


@admin.register(EmailTable)
class EmailTableAdmin(admin.ModelAdmin):

    list_display = ("Email", "Salary")
    search_fields = ("Email", )
    ordering = ("Created", )
