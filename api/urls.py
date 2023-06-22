from django.urls import path, include
from .views import *

# api/

urlpatterns = [
    path('generate', CreateDataView.as_view(), name='generate'),
    path('', landing, name='landing_page'),
]   
