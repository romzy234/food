from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yam', views.yam, name='yam'),
    path('egg', views.egg, name='egg'),
    path('spa', views.spa, name='spa'),
]