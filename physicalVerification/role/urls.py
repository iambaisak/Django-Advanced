from django.urls import path
from .views import RoleViews

urlpatterns = [
    path('', RoleViews.as_view()),
    path('role/', RoleViews.as_view()),
    path('role/<int:id>', RoleViews.as_view())
]