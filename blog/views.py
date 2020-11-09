from django.shortcuts import render
from django.http import response, HttpResponse, JsonResponse
from blog.model.blog.blog_management_model import BlogManagement

# Create your views here.
BlogManagement.get_list_of_blogs()
BlogManagement.get_blog_by_id(id)