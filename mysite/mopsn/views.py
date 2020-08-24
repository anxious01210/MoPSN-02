from django.shortcuts import render
from mopsn.models import *
from django.views.generic import *

# Create your views here.

def home_v(request):
    ps4 = Ps4.objects.all()
    # ps4 = "Hello"
    context = {'ps4': ps4}
    return render(request, 'mopsn/home.html', {'ps4': ps4})


def ps4_v(request):
    ps4 = Ps4.objects.all()
    # ps4 = "Hello"
    context = {'ps4': ps4}
    return render(request, 'mopsn/ps4.html', {'ps4': ps4})

def netflix_v(request):
    print('Netflix: ', )
    # netflix = Netflix.objects.all().order_by[-"publish_date"]
    acc_netflix = Netflix.objects.all()
    # ps4 = "Hello"
    # context = {'netflix': acc_netflix}
    return render(request, 'mopsn/netflix.html', {'netflix': acc_netflix})

# def nety_v(request):
#     print('Nety: ')
#     nety = Nety.objects.all()
#     # acc_netflix = Netflix.objects.all()
#     # ps4 = "Hello"
#     # context = {'netflix': acc_netflix}
#     return render(request, 'mopsn/nety.html', {'nety':nety,})

def nintendo_v(request):
    nintendo = Nintendo.objects.all()
    # ps4 = "Hello"
    context = {'nintendo': nintendo}
    return render(request, 'mopsn/nintendo.html', {'nintendo': nintendo})
