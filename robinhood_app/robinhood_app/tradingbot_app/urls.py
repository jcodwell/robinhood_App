from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .apiViews import AboutInfo_CryptoModelViewSet



router = DefaultRouter()
router.register(r'aboutInfo', AboutInfo_CryptoModelViewSet, basename='aboutInfo')
urlpatterns = [
    path('', include(router.urls))
]

