from django.urls import path
from. import views


urlpatterns = [
    path('', views.index),
    path('dooly', views.dooly),
    path('pororo', views.pororo),
]