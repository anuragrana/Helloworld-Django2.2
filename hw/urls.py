from django.urls import path

from . import views

app_name = "hw"
urlpatterns = [
    path(r'', views.home, name='home'),
]