from django.db import models
from django.contrib.auth.models import User
from flearn.models import Course


class MyCourse(models.Model):
    student = models.ManyToManyField(User, related_name='courses')
    course = models.ForeignKey(Course, related_name='students',
                               on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name