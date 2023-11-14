from django.urls import path

from .views import login, parse_excel

urlpatterns = [
    path('login/', login, name='login'),
    path('parse/', parse_excel, name='parse'),
]