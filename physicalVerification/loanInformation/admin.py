from django.contrib import admin

from .models import LoanApplication
from .models import LoanApplicationHistory

admin.site.register(LoanApplication)
admin.site.register(LoanApplicationHistory)