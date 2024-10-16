from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

def home_page(request):
    return HttpResponse("HI")



def super_user_login_page(request):
    if request.user.is_authenticated :
        redirect('home')


def login_user_employee(request):
    if request.method == "POST":

        return "Hi user"