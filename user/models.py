from django.db import models


class User(models.Model):
    """
    Класс - характеристика сотрудника
    """
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Кассир"
        verbose_name_plural = "Кассиры"

