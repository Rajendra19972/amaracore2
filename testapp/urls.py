from django.urls import path
from testapp import views

urlpatterns = [
    path('index/',views.index, name = 'index')
]