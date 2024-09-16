
from django.urls import path,include
from apps.tutorial import views

app_name = "tutorial"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('tutorial_details/', views.tutorial_details, name='tutorial_details'),
    
]
