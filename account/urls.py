from . import views
from django.urls import path , include
from . import views 


urlpatterns = [
      path('sign_in/' , views.sign_in1 , name='sign_in1'),
      path('sign_up/' , views.sign_up , name='sign_up')
   
    

]