from tkinter.tix import Tree
from cffi import VerificationError
from django.db import models

# Create your models here.

"""
"first_names": first_names,
"last_names": last_names,
"cellphone_nos": phone_numbers,
"email addresses": email_addresses,
"passwords": passwords
"""

class Profile(models.Model):
    
    _id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    date_of_birth = models.CharField(max_length=500)
    bio = models.TextField()
    verification_question = models.TextField()
