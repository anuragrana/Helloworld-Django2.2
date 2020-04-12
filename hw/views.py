from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from urllib.parse import parse_qs


# Create your views here.
def home(request):
    data = dict()
    return render(request, 'hw/home.html', data)


@csrf_exempt
def post_example_raw(request):
    print('POST', request.POST)
    print('BODY', request.body)
    print('JSON', json.loads(request.body.decode('utf-8')))
    print('FILES', request.FILES)
    return render(request, 'hw/home.html', {})


@csrf_exempt
def post_example_form_urlencoded(request):
    print('POST', request.POST)
    print('BODY', request.body)
    print(parse_qs(request.body.decode('utf-8')))
    return render(request, 'hw/home.html', {})


@csrf_exempt
def post_example_form_data(request):
    print('POST', request.POST)
    print('FILES', request.FILES)
    return render(request, 'hw/home.html', {})


@csrf_exempt
def post_example_binary(request):
    print('POST', request.POST)
    print('BODY', request.body)
    print('FILES', request.FILES)
    return render(request, 'hw/home.html', {})


@csrf_exempt
def post_example_none(request):
    print('POST', request.POST)
    print('BODY', request.body)
    print('FILES', request.FILES)
    return render(request, 'hw/home.html', {})


@csrf_exempt
def post_example_file_upload(request):
    print('POST', request.POST)
    print('FILES', request.FILES)
    return render(request, 'hw/home.html', {})
