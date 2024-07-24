"""
Модуль содержит представления для меню
"""

from django.shortcuts import render

from menu_app.models import Menu, MenuItem


def index(request):
    """
    Отображает главную страницу с доступными меню.
    """
    menus = Menu.objects.all()
    menu_slugs = [menu.slug for menu in menus]
    return render(request, 'menu_app/index.html', {'menu_slugs': menu_slugs})


def draw_menu(request, menu_slug):
    """
    Отображает элементы меню по заданному слагу.
    """
    menu = Menu.objects.get(slug=menu_slug)
    menu_items = MenuItem.objects.filter(menu=menu)
    return render(request, 'menu_app/menu.html', {'menu': menu, 'menu_items': menu_items})

