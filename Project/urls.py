from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sweets/', views.sweets_list, name='sweets_list'),
    path('sweets/<int:sweet_id>/', views.sweet_detail, name='sweet_detail'),
    path('about/', views.about, name='about'),
]