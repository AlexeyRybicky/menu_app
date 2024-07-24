"""
Модуль содержит настраиваемые теги шаблонов для приложения меню в Django.
Он предоставляет тег draw_menu, который позволяет отображать меню на основе заданного слага.
"""

from django import template
from menu_app.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    """
    Отображает меню на основе заданного слага.

    Этот тег извлекает меню из базы данных по его слагу и получает все элементы меню,
    связанные с этим меню. Возвращаемые данные передаются в указанный шаблон для рендеринга.

    Args:
        context (dict): Контекст шаблона, содержащий данные, доступные в шаблоне.
        menu_slug (str): Слаг меню, которое нужно отобразить.

    Return:
        dict: Словарь, содержащий следующие ключи:
        'menu_items': QuerySet объектов MenuItem, связанных с указанным меню.
        'menu_slug': Название меню, соответствующее переданному слагу.
        'menu_slugs': Список слогов меню из контекста, доступный для использования в шаблоне.
    """
    menu = Menu.objects.get(slug=menu_slug)
    menu_items = MenuItem.objects.filter(menu=menu)
    return {
        'menu_items': menu_items,
        'menu_slug': menu.name,
        'menu_slugs': context['menu_slugs'],
    }
