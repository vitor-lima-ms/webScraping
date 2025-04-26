from django.urls import path
from brasil import views

app_name = 'brasil'
urlpatterns = [
    path('tabela/brasileirao-serie-b/', views.serieB, name='serieB'),

    path('tabela/brasileirao-serie-a/', views.serieA, name='serieA'),

    path('noticias/futebol-brasileiro/', views.noticiasBR, name='noticiasBR'),
]