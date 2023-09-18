from django.http import HttpResponse
from django.shortcuts import render

from .models import place
from .models import place1


# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=place1.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})