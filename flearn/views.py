from django.shortcuts import render
from .models import Category, SubCategory, Course
from django.http import HttpResponse


def index(request):
    # will be fixed later. 
    category = SubCategory.objects.all()[:3]
    category_business = SubCategory.objects.filter(category__name='Business')
    context = {
        'category': category,
        'category_business': category_business,
    }
    return render(request, 'flearn/index.html', context)


def categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'flearn/all_categories.html', context)


def subcategory_detail(request, slug):
    sub_category = SubCategory.objects.get(slug=slug)
    courses = sub_category.courses.all()
    context = {
        'courses': courses,
        'sub_category': sub_category,
    }
    return render(request, 'flearn/subcategory_detail.html', context)


def course(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        'course': course,
    }
    return render(request, 'flearn/course_detail.html', context)