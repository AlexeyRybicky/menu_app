"""
Модуль содержит классы для создания меню в админ панели
"""

from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    """
    Класс для отображения элементов меню в админ-панели.
    Этот класс позволяет редактировать элементы меню, связанные с родительским меню.

    Args:
        model (Model): Модель, которая будет отображаться в виде инлайна.
        extra (int): Количество дополнительных пустых форм для добавления новых элементов.
        fields (tuple): Поля, которые будут отображаться в форме инлайна.
    """
    model = MenuItem
    extra = 0
    fields = (
        'title',
        'url',
        'named_url',
        'parent'
    )

    def get_formset(self, request, obj=None, **kwargs):
        """
        Переопределяет метод для получения формы инлайна.
        Добавляет фильтрацию по родительскому элементу меню,
        чтобы показывать только элементы меню, относящиеся к текущему меню.

        Return:
            formset: Объект формы инлайна с отфильтрованным queryset для поля 'parent'
        """
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['parent'].queryset = MenuItem.objects.filter(menu=obj)
        return formset


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Класс для модели Menu.
    Настраивает отображение модели Menu в админ-панели,
    включая инлайн-редактирование связанных элементов меню.
    """
    model = Menu
    inlines = [MenuItemInline]


admin.site.register(MenuItem)
