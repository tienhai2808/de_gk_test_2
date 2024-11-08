from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('dsmonhoc/<int:idmonhoc>/', ctmonhoc),
    path('dssinhvien/<int:idsinhvien>/', ctsinhvien, name='ctsinhvien'),
    path('suasinhvien/<int:idsinhvien>/', sinhvien),
    path('taosinhvien/', sinhvien)
]