from django.db import models


class Product(models.Model):

    title = models.CharField('Заказ', max_length=50)
    product_num = models.IntegerField('Количество')
    price = models.DecimalField('Цена', max_digits=30, decimal_places=2, default=0)
    total_price = models.DecimalField('Итого', max_digits=30, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class ProductImage(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_menu_image = models.ImageField(upload_to='images/')
    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"