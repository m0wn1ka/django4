from django.db import models

# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   phone = models.IntegerField()
#   joined_date = models.DateField()
class student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    branch =models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    idno=models.CharField(max_length=255)
    atte=models.IntegerField()
    grade=models.CharField(max_length=255)
    marks=models.IntegerField()
