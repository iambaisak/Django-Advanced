from django.db import models
from loanInformation.models import LoanApplication

# Create your models here.
class VerificationDocument(models.Model):
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='loan_application_id')
    document_type = models.CharField(max_length=100,
                              choices=(
                                  ("applicant_photo", "applicant_photo"),
                                  ("address_proof", "address_proof"),
                                  ("dob_proof", "dob_proof")
                              ))
    file_path = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_type