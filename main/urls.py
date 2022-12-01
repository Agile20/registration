from .views import *
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('registration/', RegistrationView.as_view()),
    path('login/', AutorisationView.as_view()),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


