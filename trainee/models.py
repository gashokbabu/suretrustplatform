from django.db import models
from users.models import User
# Create your models here.
class Student(models.Model):
    Choices = (
        ('male','male'),
        ('female','female')
    )
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=100,choices=Choices,default="male")  
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    registration_no = models.PositiveBigIntegerField(primary_key=True)
    profice_pic = models.ImageField(default="default.jpg",upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.name}'