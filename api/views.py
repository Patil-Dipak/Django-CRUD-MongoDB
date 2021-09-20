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
    elif request.method == "POST":
        dept_data = JSONParser().parse(request)
        dept_serializer = DeptSerializer(data = dept_data)

        if dept_serializer.is_valid():
            dept_serializer.save()
            return JsonResponse("Added Successfully", safe= True)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == "PUT":
        dept_data = JSONParser().parse(request)
        dept = Dept.objects.get(DeptId = dept_data['DeptId'])
        dept_serializer = DeptSerializer(dept, data = dept_data)

        if dept_serializer.is_valid():
            dept_serializer.save()
            return JsonResponse("Update Successfully", safe= True)
        return JsonResponse("Failed to Update",safe=False)
