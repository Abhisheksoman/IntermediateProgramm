from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)