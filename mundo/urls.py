from django.urls import path

from mundo import views

app_name = 'mundo'

urlpatterns = [
    path('', views.index, name='index'),
]