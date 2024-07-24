"""
Модуль содержит конфигурацию маршрутов приложения `menu_app`
"""

from django.urls import path
from menu_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<slug:menu_slug>/', views.draw_menu, name='menu'),
]