from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('auth/', views.signup, name='signup'),
    path('logview/', views.logview, name='logview'),
]