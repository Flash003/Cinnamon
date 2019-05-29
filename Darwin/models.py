from django.db import models
from django.contrib.auth.models import User
import datetime

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles', default='profiles/default_user.jpg')
    gender = models.CharField(max_length=7, choices = (('male', 'male'),('female', 'female')))
    dob = models.DateTimeField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    login_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.first_name



class Disease(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=120)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Store(models.Model): 
    name = models.CharField(max_length=50) 
    main_Img = models.ImageField(upload_to='images/')