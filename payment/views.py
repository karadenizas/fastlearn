import braintree
from braintree import client_token
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import PurchasedCourse
from account.models import MyCourse
from flearn.models import Course
from .tasks import payment_success


gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request, id):
    user = request.user
    course = Course.objects.get(id=id)
    my_course = MyCourse.objects.get_or_create(course=course)
    my_course = MyCourse.objects.get(course=course)
    #if user in my_course.student.all():
    #    return HttpResponse(f'{user} have this course.')
    #else:
    #    return HttpResponse(f'{user} buying is success!')
    #return HttpResponse(course.price)
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        result = gateway.transaction.sale({
            'amount': course.price,
            'payment_method_nonce': nonce,
            'options': {'submit_for_settlement': True}
        })
        if result.is_success:
            my_course.student.add(user)
            course = course.name
            user = user.username
            user_mail = request.user.email
            payment_success.delay(course, user, user_mail)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = gateway.client_token.generate()
        context = {
            'client_token': client_token
        }
        return render(request, 'payment/process.html', context)


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')