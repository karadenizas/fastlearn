from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import MyCourse
from flearn.models import Video


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', 
                                            {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    context = {
        'user_form': user_form
    }
    return render(request, 'account/register.html', context)


def account(request):
    return render(request, 'account/account.html')


def my_courses(request, course=None):
    if course:
        user = request.user
        course = MyCourse.objects.filter(student=user).get(course__name=course)
        videos = course.course.videos.all()
        context = {
            'course': course,
            'videos': videos,
        }
        return render(request, 'account/watch_course.html', context)

    else:
        user = request.user
        my_courses = MyCourse.objects.filter(student=user)
        #my_videos = 
        #return HttpResponse(my_videos)
        context = {
            'my_courses': my_courses,
            #'my_videos': my_videos
        }
        return render(request, 'account/mycourses.html', context)