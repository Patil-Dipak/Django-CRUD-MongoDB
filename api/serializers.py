from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Dept,Employee

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = ['DeptId','DeptName']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['EmployeetId','EmployeetName','Dept','DateOfJoining']