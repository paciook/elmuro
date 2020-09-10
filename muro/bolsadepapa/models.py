from django.db import models

# Create your models here.

class Mensaje(models.Model):
	msg = models.CharField(max_length=200)
