from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Dept, Employee
from .serializers import DeptSerializer, EmployeeSerializer
# Create your views here.

@csrf_exempt
def deptApi(request, id = 0 ):
    if request.method == "GET":
        dept = Dept.objects.all()
        dept_serializers = DeptSerializer(dept, many = True)
        return JsonResponse(dept_serializers.data, safe = True)
    