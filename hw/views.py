from django.shortcuts import render


# Create your views here.
def home(request):
    data = dict()
    return render(request, 'hw/home.html', data)


def get_request_example(request):
    # print complete QueryDict
    print(request.GET)
    # print one value of param1
    print(request.GET.get('param1'))
    # print whole list of values for param1
    # print(request.GET.getlist('param1'))
    return render(request, 'hw/home.html', {})
