from django.db import models
from core.models import Base
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.


class User(Base, AbstractUser):
    CUSTOMERUSER_EMPLOYEE = 'employee'
    CUSTOMERUSER_CUSTOMER = 'customer'
    CUSTOMERUSER_MANAGER = 'manager'
    CUSTOMERUSER_STATUS = (
        (CUSTOMERUSER_EMPLOYEE,'EMPLOYEE'),
        (CUSTOMERUSER_CUSTOMER,'CUSTOMER'),
        (CUSTOMERUSER_MANAGER,'MANAGER')
    )
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    mobile_regex = RegexValidator(regex='^(\+98|0)?9\d{9}$', message="Phone number must be entered in the format: '+989199999933'.")
    phone_number = models.CharField(validators=[mobile_regex], max_length=20, unique=True)
    birthday = models.PositiveIntegerField(default=0)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    user_type = models.CharField(max_length=8,choices=CUSTOMERUSER_STATUS, default=CUSTOMERUSER_CUSTOMER)
    image = models.ImageField(upload_to='covers/', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

class Address(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user}-{self.city}'
    
class OtpCode(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_otp')
    code=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.user}-{self.code}'