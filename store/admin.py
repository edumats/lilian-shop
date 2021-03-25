from django.contrib import admin

from .models import Hantem


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Hantem, ProductAdmin)
