from operator import truediv
from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    msg = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.full_name
