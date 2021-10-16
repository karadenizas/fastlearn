from django.urls import path
from . import views

app_name = 'instructor'

urlpatterns = [
    path('', views.instructor, name='instructor'),
    path('edit/<str:course>/', views.edit, name='course_edit'),
]