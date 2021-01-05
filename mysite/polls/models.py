from django.db import models


class Student(models.Model):
    studentid = models.IntegerField(default=0)
    name = models.CharField(max_length=120)
    major = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    location = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/')
    class Meta:
        db_table = "student"
