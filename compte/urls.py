from django.urls import path
from . import views

app_name = 'compte'

urlpatterns = [
    path('compte/', views.compte, name='compte'),
    path('modifier-compte/', views.modifier_compte, name='modifier_compte'),

]
