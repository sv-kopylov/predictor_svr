from django.urls import path
from . import views

urlpatterns =[
    path('prd', views.predict(), name ='predict')
]