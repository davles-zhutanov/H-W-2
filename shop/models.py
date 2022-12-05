from django.db import models

class Item(models.Model):
    name_item = models.CharField(max_length=30, verbose_name='Наименования товара')
    price = models.IntegerField(verbose_name='Цена товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name_item}'

class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name= 'ФИО клиента')
    age = models.IntegerField(verbose_name= 'Возраст клиента')
    item =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    date_purchase =models.DateField(auto_now_add=True, verbose_name='Дата покупки')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'{self.item.name_item} - {self.name}'

