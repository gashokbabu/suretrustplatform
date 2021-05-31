from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class User(AbstractUser):
    username=None
    email = models.EmailField(max_length=254,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    

    def __str__(self):
        return f'{self.email}'