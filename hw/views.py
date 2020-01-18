from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def home(request):
    data = dict()
    messages.success(request, "Success: This is the sample success Flash message.")
    messages.error(request, "Error: This is the sample error Flash message.")
    messages.info(request, "Info: This is the sample info Flash message.")
    messages.warning(request, "Warning: This is the sample warning Flash message.")
    return render(request, 'hw/home.html', data)
