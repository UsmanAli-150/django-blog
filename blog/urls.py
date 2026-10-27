from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('contact/',views.contact,name='contact'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<str:name>/', views.post_filter, name='post_filter'),
    path('post/', views.latest_posts, name='latest_post') 
]