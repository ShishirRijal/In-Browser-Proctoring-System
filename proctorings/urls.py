from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('video_feed/', views.video_feed, name='video_feed'),  # Add this line for video feed
    path('stop_video_feed/', views.stop_video_feed, name='stop_video_feed'),
    path('about/', views.about, name='about'),  # Add this line
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
