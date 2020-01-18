from django.shortcuts import render


# Create your views here.
def home(request):
    data = dict()
    return render(request, 'hw/home.html', data)
