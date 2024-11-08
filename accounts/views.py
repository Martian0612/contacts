from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

# Creating an api using this decorator.
@api_view()
def send_otp(request):
    if request.data('phone_number') is None:
        response = {
            'status': 400,
            'message':'Phone number is required.'
        }
        return response

    if request.data('password') is None:
        response = {
            'status' : 400, 
            'message' : 'Password required.'
        }
        return response
    
    user = User(
        phone_number = phone_number
        
        )