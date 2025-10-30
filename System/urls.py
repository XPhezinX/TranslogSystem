from django.urls import path
from System.views import casdastro_pessoas
urlpatterns = [
    path('', casdastro_pessoas),
]
