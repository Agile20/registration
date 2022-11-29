from .views import *
from django.urls import path 



urlpatterns =[
    path('registration/', RegistrationView.as_view()),
    path('login/', AutorisationView.as_view()),
]





