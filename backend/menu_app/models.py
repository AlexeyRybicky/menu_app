"""
Модуль содержит модели бызы данных
"""

from django.db import models


class Menu(models.Model):
    """
    Модель для представления меню.
    """

    objects: models.Manager

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # pylint: disable=missing-docstring
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    # pylint: disable=E1101
    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    """
    Модель для представления элемента меню.
    """
    objects: models.Manager

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255, default='')
    url = models.CharField(max_length=255)
    named_url = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    # pylint: disable=missing-docstring
    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    # pylint: disable=E1101
    def __str__(self) -> str:
        return self.title

    def get_children(self) -> models.QuerySet:
        """
        Метод для получения всех дочерних элементов текущего элемента меню.
        """
        return self.children.all()
