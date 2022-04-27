from unicodedata import name
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'plants', views.MyPlantSet)
router.register(r'ferns', views.MyFernSet, 'ferns')
router.register(r'succulents', views.MySucculentSet, 'succulents')
router.register(r'vines', views.MyVineSet, 'vines')
router.register(r'shoppers', views.MyShopperSet, 'shoppers')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
    ]