from django.urls import path

from . import views

app_name = "hw"
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'post-example/raw/', views.post_example_raw, name='post_example_raw'),
    path(r'post-example/form-urlencoded/', views.post_example_form_urlencoded, name='post_example_form_urlencoded'),
    path(r'post-example/form-data/', views.post_example_form_data, name='post_example_form_data'),
    path(r'post-example/binary/', views.post_example_binary, name='post_example_binary'),
    path(r'post-example/none/', views.post_example_none, name='post_example_none'),
    path(r'post-example/file-upload/', views.post_example_file_upload, name='post_example_file_upload'),

]