from django.shortcuts import render
from django.http import response, HttpResponse, JsonResponse
from user.model.user.user_management_model import UserManagement

# Create your views here.
UserManagement.get_list_of_users()
UserManagement.get_user_by_id(id)