from django.urls import path
from .views import VerificationDocumentViews

urlpatterns = [
    path('', VerificationDocumentViews.as_view()),
    path('verificationDocument/', VerificationDocumentViews.as_view()),
    path('verificationDocument/<int:id>', VerificationDocumentViews.as_view())
]