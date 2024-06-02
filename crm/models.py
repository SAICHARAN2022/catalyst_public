from django.db import models

# Create your models here.
from datetime import datetime


class CompanyData(models.Model):
    keyword = models.CharField(max_length=255,null=True)
    name = models.CharField(max_length=255,null=True)
    domain = models.CharField(max_length=255,null=True)
    year_founded = models.CharField(max_length=255,null=True)
    size_range = models.CharField(max_length=255,null=True)
    locality = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    linked_url = models.CharField(max_length=255,null=True)
    industry = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    current_emplyee_estimate = models.IntegerField(null=True)
    total_emplyee_estimate = models.IntegerField(null=True)
    emplyee_from = models.DateTimeField(auto_now_add=True)
    emplyee_to = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'crm_companies'    
