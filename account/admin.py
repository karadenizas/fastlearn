from django.contrib import admin
from .models import MyCourse


@admin.register(MyCourse)
class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'created']