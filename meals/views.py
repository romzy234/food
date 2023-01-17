from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def yam(request):
    return render(request, 'yam.html')
def egg(request):
    return render(request, 'egg.html')

def spa(request):
    return render(request, 'spa.html')