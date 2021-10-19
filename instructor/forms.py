from django import forms
from django.forms import fields, widgets
from flearn.models import Course, Video


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['sub_category', 'name', 'description', 'price', 'image']