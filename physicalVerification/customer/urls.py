from django.urls import path
from .views import CustomerViews

urlpatterns = [
    path('', CustomerViews.as_view()),
    path('customer/', CustomerViews.as_view()),
    path('customer/<int:id>', CustomerViews.as_view())
]