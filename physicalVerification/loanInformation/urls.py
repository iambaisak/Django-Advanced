from django.urls import path
from .views import LoanApplicationHistoryViews
from .views import LoanApplicationViews

urlpatterns = [
    path('', LoanApplicationViews.as_view()),
    path('loanApplication/', LoanApplicationViews.as_view()),
    path('loanApplication/<int:id>', LoanApplicationViews.as_view()),
    path('history', LoanApplicationHistoryViews.as_view()),
    path('loanApplicationHistory/', LoanApplicationHistoryViews.as_view()),
    path('loanApplicationHistory/<int:id>', LoanApplicationHistoryViews.as_view())
]