"""
Модуль содержит конфигурацию для приложения `menu_app`
"""

from django.apps import AppConfig


class MenuAppConfig(AppConfig):
    """
    Класс конфигурации приложения `menu_app`
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu_app'
    verbose_name = 'Приложение Меню'
