from django.urls import path
from .views import EmployeeViews

urlpatterns = [
    path('', EmployeeViews.as_view()),
    path('employee/', EmployeeViews.as_view()),
    path('employee/<int:id>', EmployeeViews.as_view())
]