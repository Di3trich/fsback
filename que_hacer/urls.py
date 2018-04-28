from django.urls import path
from . import views

app_name = 'que_hacer'
urlpatterns = [
    path('', views.index, name='index'),
    path('registro/<int:grupo_id>/', views.registro, name='registro'),
]
