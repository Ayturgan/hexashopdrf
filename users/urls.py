from django.urls import path
from .views import register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import register
urlpatterns = [
    path('register/', register),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

