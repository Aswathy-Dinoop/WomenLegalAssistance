from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)
class PeopleRights(models.Model):
    rights=models.CharField(max_length=50,null=True)
    desc=models.CharField(max_length=50,null=True)
    image=models.ImageField(max_length=50,null=True)
class UserRegistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True) 
    password=models.CharField(max_length=50,null=True)
class AdvocateRegistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    rights=models.ForeignKey(PeopleRights,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True) 
    image=models.ImageField(max_length=50,null=True)
    regnum=models.CharField(max_length=50,null=True)
    exp=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class Petition(models.Model):
    user=models.ForeignKey(UserRegistration,on_delete=models.CASCADE,null=True)
    lawyer=models.ForeignKey(AdvocateRegistration,on_delete=models.CASCADE,null=True)
    complaint=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    reply=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
