from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.transaction)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'transaction_date', 'user_id')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.category)    