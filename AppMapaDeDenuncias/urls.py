from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapa_denuncias, name='mapa_denuncias'),
    path('api/denuncias/', views.api_denuncias, name='api_denuncias'),
    path('denuncia/<int:denuncia_id>/', views.detalhe_denuncia, name='detalhe_denuncia'),
]