from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(max_length=15)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name


    class Meta:
        db_table = "user"

