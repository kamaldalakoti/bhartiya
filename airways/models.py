from datetime import date
from django.db import models

# Create your models here.
class applied(models.Model):
    Name = models.CharField(max_length=200 , null=True)
    Email = models.EmailField(max_length=200 , null=True)
    Mobile = models.CharField(max_length=200 , null=True)
    Address = models.CharField(max_length=200 , null=True)
    City = models.CharField(max_length=200 , null=True)
    State = models.CharField(max_length=200 , null=True)
    Reference = models.CharField(max_length=20, null=True)
    resume = models.FileField(upload_to='static/resume' , null=True)
    Date = models.DateField(default=date.today)
    trm = models.CharField(max_length=100 , null=True)


class contact(models.Model):
    Email = models.CharField(max_length=100 , null=True)
    Name = models.CharField(max_length=100 , null=True)
    Phone = models.CharField(max_length=100 , null=True)
    Message = models.CharField(max_length=500 , null=True)
    Subject = models.CharField(max_length=100 , null=True)
