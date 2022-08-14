from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name 

class ApplicantInfo(models.Model):
    CHOICES = (
    ('O','O'),
    ('A', 'A'),
    ('B' ,'B'),
    ('AB','AB'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/applicants', blank=True, null=True)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    blood = models.CharField(choices=CHOICES, max_length=5)
    citizenshipno = models.CharField(max_length=50)
    citizenshipdate = models.DateField()
    citizenshipdistrict = models.CharField(max_length=200)
    citizenship = models.ImageField(upload_to='media/citizenship', blank=True, null=True)
    zone = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=3)
    tole = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname + self.lastname
    
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/defaultuser.jpg"

class License(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.category) + ' - ' + str(self.applicant.username)
    
