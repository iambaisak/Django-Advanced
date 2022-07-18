from .models import LoanApplication
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LoanApplicationHistory


@receiver(post_save, sender=LoanApplication, dispatch_uid='signal_receiver')
def create_loan_application_history(sender, instance, **kwargs):
    loan_application_id = instance.id
    customer_id = instance.customer.id
    status = instance.status
    verification_status = instance.verification_status
    manager_id = instance.manager.id
    verifier_id = instance.verifier.id
    reviewer = instance.reviewer.id
    loan_amount = instance.loan_amount
    LoanApplicationHistory.objects.create(loan_application_id=loan_application_id, customer_id=customer_id,
                                          status=status, verification_status=verification_status, manager_id=manager_id,
                                          verifier_id=verifier_id, reviewer=reviewer, loan_amount=loan_amount)