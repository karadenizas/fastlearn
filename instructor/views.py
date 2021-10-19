from django import http
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
from flearn.models import Course, Video
from .forms import CourseEditForm
from django.forms import modelformset_factory
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        PermissionRequiredMixin)
from django import forms
from django.urls import reverse_lazy


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



@login_required
@permission_required(perm=('flearn.add_course',
                     'flearn.change_course',
                     'flearn.delete_course',
                     'flearn.view_course'), raise_exception=True)
def video_edit(request, course):
    user = request.user
    if user == Course.objects.get(name=course).instructor:
        ArticleFormset = modelformset_factory(Video, fields=('name', 'video'), extra=0)
        formset = ArticleFormset(queryset=Video.objects.filter(course__name=course))
        if request.method == "POST":
            formset = ArticleFormset(request.POST, request.FILES)
            if formset.is_valid():
                formset.save()
                return redirect('instructor:instructor')
        context = {
            'formset': formset,
        }
        return render(request, 'instructor/video_edit.html', context)
    else:
        return redirect('flearn:index')



class CreateCourseView(LoginRequiredMixin,
                       PermissionRequiredMixin,
                       CreateView):
    login_url = 'login'
    permission_required = ('flearn.add_course',
                           'flearn.change_course',
                           'flearn.delete_course',
                           'flearn.view_course')
    model = Course
    fields = ['sub_category', 'name', 'image', 'instructor', 'description', 'price']
    template_name = 'instructor/course_create.html'
    success_url = '/instructor/'
    
    def get_form_kwargs(self):
        return super().get_form_kwargs()

    def get_form(self, form_class=None):
        form = super(CreateCourseView, self).get_form(form_class)
        form.fields['instructor'].widget = forms.HiddenInput()
        return form

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['instructor'] = self.request.user
        return initial


class DeleteCourseView(CreateCourseView, DeleteView):
    model = Course
    template_name = 'instructor/delete.html'