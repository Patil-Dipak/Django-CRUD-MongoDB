from django.db import models

# Create your models here.

class Dept(models.Model):
    DeptId = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=500)

class Employee(models.Model):
    EmployeetId = models.AutoField(primary_key=True)
    EmployeetName = models.CharField(max_length=500)
    Dept = models.CharField(max_length=500)
    DateOfJoining = models.DateField()