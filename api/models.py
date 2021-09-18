from django.db import models

# Create your models here.

class Dept(models.Model):
    DeptId = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=500)

