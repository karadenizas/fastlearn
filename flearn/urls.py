from django.urls import path
from . import views

app_name = 'flearn'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='all_categories'),
    path('course/<str:slug>/', views.course, name='course_detail'),
    path('subcategories/<str:slug>/', views.subcategory_detail, name='subcategory_detail'),
]