from django.urls import path
from .views import lista_aulas, reserva_aula

urlpatterns = [
    path('', lista_aulas, name='lista_aulas'),
    path('reservar/', reserva_aula, name='reserva_aula'),
    # Otros patrones de URL
]