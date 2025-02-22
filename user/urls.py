from django.urls import path
from . import views  # Import your views

app_name= 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
