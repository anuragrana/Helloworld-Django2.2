from django.urls import path

from . import views

app_name = "hw"
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'get-request-example/', views.get_request_example, name='get_request_example'),
]
