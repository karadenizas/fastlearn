from django.contrib import admin
from .models import Category, SubCategory, Course, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ['name', 'sub_category', 'slug', 'price']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']