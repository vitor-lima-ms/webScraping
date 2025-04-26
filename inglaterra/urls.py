from django.urls import path
from inglaterra import views

app_name = 'inglaterra'
urlpatterns = [
    path('tabela/premier-league/', views.premierLeague, name='premierLeague'),

    path('noticias/premier-league/', views.noticiasPremeierLeague, name='noticiasPremeierLeague'),
]