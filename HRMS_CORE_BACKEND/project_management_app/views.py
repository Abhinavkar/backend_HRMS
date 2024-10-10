from django.http import HttpResponse
from django.shortcuts import redirect
# from .models import User
# Create your views here.
def home_page(request):
    return HttpResponse("HI")



def super_user_login_page(request):
    if request.user.is_authenticated :
        redirect('home')