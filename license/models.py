from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name 

class ApplicantInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    midname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    blood = models.CharField(max_length=3)
    citizenshipno = models.CharField(max_length=50)
    citizenshipdate = models.DateField()
    citizenshipdistrict = models.CharField(max_length=200)
    citizenship = models.ImageField()
    zone = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=3)
    tole = models.CharField(max_length=200)

class License(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    applicant = models.ForeignKey(ApplicantInfo, on_delete=models.CASCADE)
    
