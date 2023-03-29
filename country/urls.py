from django.urls import path , include
from . import views 

urlpatterns = [
     path('' , views.country , name='country' ),
    path('<int:id>' , views.index , name='index'),
    path('test/' , views.country1 , name='country1' ),
    
    
   
]
