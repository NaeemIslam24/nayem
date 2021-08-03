from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Technology)


@admin.register(Portfolio)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "client_name")
    prepopulated_fields = {"slug": ("title",)}
