from django.db import models


class User(models.Model):
    """
    Класс - характеристика сотрудника
    """
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    position = models.CharField('Позиция', max_length=50)
    time_create = models.DateTimeField('Создан', auto_now_add=True)
    time_update = models.DateTimeField('Обновлен', auto_now=True)
    def __str__(self):
        return str(self.surname) + ' '  + str(self.name)
    class Meta:
        verbose_name = "Кассир"
        verbose_name_plural = "Кассиры"

