from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('grupo', views.GrupoViewSet)
router.register('quehacer', views.QueHacerViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/<int:grupo_id>/', views.registro, name='registro'),
    path('realizado/<int:quehacer_id>/', views.realizado, name='realizado'),
    path('eliminar/<int:quehacer_id>/', views.eliminar, name='eliminar'),
    path('api/', include(router.urls)),
    path('api-login/', include('rest_framework.urls', namespace='rest_framework')),
]
