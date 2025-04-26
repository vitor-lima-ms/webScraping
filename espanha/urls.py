from django.urls import path
from espanha import views

app_name = 'espanha'

urlpatterns = [
    path('tabela/laliga/', views.laLiga, name='laLiga'),

    path('noticias/laliga/', views.noticiasLaLiga, name='noticiasLaLiga'),
]