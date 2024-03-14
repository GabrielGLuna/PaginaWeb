from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def especificaciones(request):
    return render(request, 'home/especificaciones.html')

def tutorial(request):
    return render(request, 'home/tutorial.html')
