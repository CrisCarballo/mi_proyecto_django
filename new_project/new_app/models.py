from typing import Any
from django.db import models

# Create your models here.

class Employee(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    hire_date = models.DateField()
    is_admin = models.BooleanField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"