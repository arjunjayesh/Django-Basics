from . import views
from django.urls import path, include
app_name='credentials'

urlpatterns = [
    path('register/', views.register, name='register'),
]