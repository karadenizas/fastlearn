from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
from flearn.models import Course
from django.contrib.auth.models import User
from .forms import CourseEditForm


@login_required
@permission_required(perm=('flearn.add_course',
                     'flearn.change_course',
                     'flearn.delete_course',
                     'flearn.view_course'), raise_exception=True)
def instructor(request):
    user = request.user
    my_courses = Course.objects.filter(instructor=user)
    context = {
        'my_courses': my_courses,
    }
    return render(request, 'instructor/instructor_index.html', context)


@login_required
@permission_required(perm=('flearn.add_course',
                     'flearn.change_course',
                     'flearn.delete_course',
                     'flearn.view_course'), raise_exception=True)
def edit(request, course):
    user = request.user
    my_course = Course.objects.get(name=course, instructor=user)
    form = CourseEditForm(initial={'name': my_course.name,
                                   'description': my_course.description,
                                   'sub_category': my_course.sub_category,
                                   'price': my_course.price,
                                   'image': my_course.image})
    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            my_course.name = cd['name']
            my_course.description = cd['description']
            my_course.sub_category = cd['sub_category']
            my_course.price = cd['price']
            if cd['image']:
                my_course.image = cd['image']
            else:
                my_course.save()    
            my_course.save()
            return redirect('instructor:instructor')
            #slug field will be edited

    context = {
        'my_course': my_course,
        'form': form,
    }
    return render(request, 'instructor/course_edit.html', context)