
from django.urls import path
from .views import main , test_page

urlpatterns = [
    path('', main, name="main"),  
    path('test/', test_page),  
]