from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('info/<int:id>/', info, name='info'),
    path('delete/<int:id>/', delete, name='delete'),
]
