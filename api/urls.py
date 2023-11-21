from django.urls import path

from .views import login, parse_excel, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('parse/', parse_excel, name='parse'),
]