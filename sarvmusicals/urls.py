"""sarvmusicals URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('signup/', user_views.registerPage, name='USERS-signup'),
    path('', user_views.loginPage, name='USERS-login'),
    path('login/', user_views.loginPage, name='USERS-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='USERS-logout'),
    path('dashboard/', user_views.dashboard, name='USERS-dashboard')
]
