from django.shortcuts import render
from django.http import HttpResponse
from .models import Human


def home(request):
    return render(request, 'django_hw/home.html')

def human(request):
    hum2 = Human.objects.get(id = 2)
    return render(request,'django_hw/human.html',{'context':hum2})




# Create your views here.
