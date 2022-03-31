from django.db import models

class Product(models.Model):
    """
    Класс продукта, от него можно отнаследовать разные типы продуктов
    """
    title = models.CharField('Заказ', max_length=50)
    product = models.CharField('Количество', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
