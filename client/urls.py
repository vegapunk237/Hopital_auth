from django.contrib.auth import views as auth_views

from django.urls import include ,path

from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logged_outt.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
]