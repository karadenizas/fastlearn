from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('', include('django.contrib.auth.urls')),
    path('', views.account, name='account'),
    path('register/', views.register, name='register'),
]