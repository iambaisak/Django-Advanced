from django.db import models
from role.models import Role
# Create your models here.
class Employee(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, related_name='role_id')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.first_name + " " + self.middle_name + " " + self.last_name