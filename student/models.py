from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    student_profile = models.ImageField(null=True, blank=True, upload_to='student_profile/')