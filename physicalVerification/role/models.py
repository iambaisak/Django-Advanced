from django.db import models

# Create your models here.
class Role(models.Model):
    role_type = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)