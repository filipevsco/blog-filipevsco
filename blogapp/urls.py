from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('/about/', views.about, name="about"),
    path('/post/', views.post, name="post"),
    path('/contact/', views.contact, name="contact"),

]
