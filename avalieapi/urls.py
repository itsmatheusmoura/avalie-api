from django.urls import include, path
from rest_framework import routers

from avalieapi.empresa import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'perguntas', views.PerguntaViewSet)
router.register(r'avaliacoes', views.AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]