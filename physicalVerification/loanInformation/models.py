from django.db import models
from customer.models import Customer
from employee.models import Employee


class CommonInformation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class LoanApplication(CommonInformation):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='customer_id')
    status = models.CharField(max_length=100,
                                           choices=(
                                               ("new","new"),
                                               ("verification_pending","verification_pending"),
                                               ("approved","approved"),
                                               ("rejected", "rejected"),
                                               ("disturbed","disturbed")

                                           ))
    verification_status = models.CharField(max_length=100,
                                           choices=(
                                               ("new","new"),
                                               ("assigned","assigned"),
                                               ("verified","verified"),
                                               ("failed", "failed"),
                                               ("approved","approved"),
                                               ("rejected", "rejected")
                                           ))
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='manager')
    verifier = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='verifier')
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='reviewer')
    loan_amount = models.CharField(max_length=100)



    def __str__(self):
        return self.customer.first_name + " " + self.loan_amount


class LoanApplicationHistory(CommonInformation):
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='history_loan_application_id')
    customer_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100,
                                           choices=(
                                               ("new","new"),
                                               ("verification_pending","verification_pending"),
                                               ("approved","approved"),
                                               ("rejected", "rejected"),
                                               ("disturbed","disturbed")
                                           ))
    verification_status = models.CharField(max_length=100,
                                           choices=(
                                               ("new","new"),
                                               ("assigned","assigned"),
                                               ("verified","verified"),
                                               ("approved","approved"),
                                               ("rejected", "rejected")
                                           ))
    manager_id = models.CharField(max_length=250)
    verifier_id = models.CharField(max_length=250)
    reviewer = models.CharField(max_length=250)
    loan_amount = models.CharField(max_length=100)
