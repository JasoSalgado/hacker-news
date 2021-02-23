"""codingnews/urls.py"""

# Django modules
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

# My modules
from apps.core.views import signup
from apps.story.views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
