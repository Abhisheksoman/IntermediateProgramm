from django.db import models

# Create your models here.
class Language(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"

	class Meta:
		db_table = "language"