from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=23)
    ename= models.CharField(max_length=100)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=35)
    class Meta:
        db_table='employee'