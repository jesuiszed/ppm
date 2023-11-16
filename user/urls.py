from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('tri/', views.tri, name='tri'),
    path('activite/<int:activite_id>/', views.detail, name='detail'),
    path('reservation/<int:activite_id>/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
]
