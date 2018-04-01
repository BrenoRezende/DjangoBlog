from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.artigos_view, name='listar'),
    path('<str:slug>/', views.artigo_detalhe_view, name='detalhes')
]