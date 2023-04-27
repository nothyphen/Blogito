from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutMe, name='aboutme'),
    path('contact/', views.ContactMe, name='contactme'),
    path('<slug:slug>/', views.post_detail, name='post_details'),
]