import json
from django.forms import model_to_dict
from django.http import JsonResponse
from .models import Employee
from django.shortcuts import render


# Create your views here.


def create_employee(request):
    body = json.loads(request.body.decode('utf-8'))
    employee = Employee(**body)
    employee.save()
    return JsonResponse(model_to_dict(employee))


def get_employee(request):
    emp = Employee.objects.all().values()
    return JsonResponse(list(emp), safe=False)


def update_role_view(request):
    body = json.loads(request.body.decode('utf-8'))
    role_obj = Employee.objects.get(role_id=body["role_id"])
    role_obj.name = body['name']
    role_obj.status_id = body["status_id"]
    role_obj.save()
    return JsonResponse(model_to_dict(role_obj))
