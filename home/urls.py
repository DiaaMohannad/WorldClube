from . import views
from django.urls import path , include 

urlpatterns = [
    path('' , views.home , name='home'),
    path('sign_in/' , views.log_in , name='log_in'),
    path('sign_up/' , views.sign_up , name='sign_up'),
]
