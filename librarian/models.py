from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class LibrarianProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(null=True, blank=True)


class Book(models.Model):
    choices = (
        ('BORROWED', 'BORROWED'),
        ('AVAILABLE', 'AVAILABLE')
    )
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    book_status = models.CharField(choices=choices, max_length=80,)
