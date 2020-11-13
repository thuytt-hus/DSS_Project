from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    major = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    location = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/')


