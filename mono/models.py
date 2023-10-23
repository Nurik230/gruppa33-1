from django.db import models

class Mobile(models.Model):
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефон'
    TYPE_MOBIL = (
        ("Красный", "Красный"),
        ("Белый", "Белый"),
        ("Синий", "Синий"),
        ("Черный", "Черный")
    )
    title = models.CharField(max_length=100, verbose_name='Название телефона', null=True)
    image = models.ImageField(upload_to='', verbose_name='Загрузите фото или эмблему телефона', null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Дайте описание')
    type_mobil = models.CharField(max_length=100, choices=TYPE_MOBIL, verbose_name='Выберите цвет телефона', null=True)
    cost = models.PositiveIntegerField(verbose_name='Укажите цену', null=True)
    director = models.CharField(max_length=100, verbose_name='В какой стране производиться', null=True)
    number_of_page = models.IntegerField(null=True, verbose_name='Укажите колличество')
    created_et = models.DateTimeField(auto_created=True, null=True)
    def __str__(self):
        return (f'Название телефона-{self.title}\n'
                f'Цена телефона{self.cost}')




