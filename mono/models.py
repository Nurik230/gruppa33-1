from django.db import models
from mono.constans import TYPE_MOBIL

class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Хештег"
        verbose_name_plural = "Хештеги"




class Mobile(models.Model):
    """ References """
    hashtag = models.ManyToManyField(Hashtag)

    """ Base fields"""
    title = models.CharField(max_length=100, verbose_name='Название телефона', null=True)
    image = models.ImageField(upload_to='', verbose_name='Загрузите фото или эмблему телефона', null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Дайте описание')
    type_mobil = models.CharField(max_length=100, choices=TYPE_MOBIL, verbose_name='Выберите цвет телефона', null=True)
    cost = models.PositiveIntegerField(verbose_name='Укажите цену', null=True)
    director = models.CharField(max_length=100, verbose_name='В какой стране производиться', null=True)
    number_of_page = models.IntegerField(null=True, verbose_name='Укажите колличество')

    """ dates """
    date_start = models.DateField(verbose_name="Укажите дату издания", null=True)
    created_et = models.DateTimeField(auto_created=True, null=True)
    def __str__(self):
        return (f'Название телефона-{self.title}\n'
                f'Цена телефона{self.cost}')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефон'




class Review(models.Model):
    text = models.TextField(verbose_name='Отзывы к продуктам')
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'