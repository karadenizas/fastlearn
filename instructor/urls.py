from django.urls import path
from . import views

app_name = 'instructor'

urlpatterns = [
    path('', views.instructor, name='instructor'),
    path('edit/<str:course>/', views.edit, name='course_edit'),
    path('videoedit/<str:course>/', views.video_edit, name='video_edit'),
    path('create/', views.CreateCourseView.as_view(), name='create_course'),
    path('delete/<str:slug>/', views.DeleteCourseView.as_view(), name='delete_course'),
]