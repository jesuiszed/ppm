from django.urls import path
from park import settings
from . import views
from django.conf.urls.static import static

from .views import CustomLogoutView

app_name = 'ppm'  # Nom de l'application

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('deconnexion', CustomLogoutView.as_view(), name='deconnexion'),
    path('gestion_activites', views.gestion_activites, name='gestion_activites'),
    path('gestion_reservations', views.gestion_reservations,
         name='gestion_reservations'),
    path('gestion_personnel', views.gestion_personnel, name='gestion_personnel'),
    path('gestion_tarifs', views.gestion_tarifs, name='gestion_tarifs'),
    path('gestion_contacts', views.gestion_contacts, name='gestion_contacts'),
    path('reservations_precedentes', views.reservations_precedentes,
         name='reservations_precedentes'),
    path('gestion_stats_rapports', views.gestion_stats_rapports,
         name='gestion_stats_rapports'),
    path('gestion_equipements', views.gestion_equipements,
         name='gestion_equipements'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
