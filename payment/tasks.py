from celery import task
from django.core.mail import send_mail


@task
def payment_success(course, user, user_mail):
    subject = f'Course {course}'
    message = f'Hi {user}, you have successfully placed a course'
    mail_sent = send_mail(subject,
                         message,
                         'asdjangotest@gmail.com',
                         [user_mail])
    return mail_sent