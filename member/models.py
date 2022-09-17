from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from librarian.models import *
from datetime import datetime ,timedelta
from django.contrib.auth import  get_user_model
User = get_user_model()
class MemberProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(null=True, blank=True)

class BookBorrwed(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    
class ReturnBook(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)