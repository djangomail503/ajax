from django.urls import path
from ajax_app import views

app_name = 'app'
urlpatterns = [
    path('add_user/', views.myuser, name='add_user'),
]

 
