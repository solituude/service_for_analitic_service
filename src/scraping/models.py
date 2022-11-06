from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название района')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название района'
        verbose_name_plural = 'Название районов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Segment(models.Model):
    name = models.CharField(max_length=250, verbose_name='Сегмент')
    slug = models.CharField(max_length=250, blank=True, unique=True)

    class Meta:
        verbose_name = 'Вид сегмента'
        verbose_name_plural = 'Все виды сегмента'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Material(models.Model):
    name = models.CharField(max_length=250, verbose_name='Материал')
    slug = models.CharField(max_length=250, blank=True, unique=True)

    class Meta:
        verbose_name = 'Материал стен'
        verbose_name_plural = 'Разновидность материалов стен'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class HaveBalcony(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наличие балкона/лоджии')
    slug = models.CharField(max_length=20, blank=True, unique=True)

    class Meta:
        verbose_name = 'Наличие балкона/лоджии'
        verbose_name_plural = 'Наличие балкона/лоджии'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Conditions(models.Model):
    name = models.CharField(max_length=250, verbose_name='Состояние')
    slug = models.CharField(max_length=250, blank=True, unique=True)

    class Meta:
        verbose_name = 'Состояние квартиры'
        verbose_name_plural = 'Состояние квартир'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class CountRooms(models.Model):
    name = models.CharField(max_length=250, verbose_name='Количество комнат')
    slug = models.CharField(max_length=250, blank=True, unique=True)

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Ads(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок объявления')

    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Район', default='Не указано')

    address = models.CharField(max_length=250, verbose_name='Местоположение')
    price = models.IntegerField(verbose_name='Стоимость', default=0)
    company = models.CharField(max_length=250, verbose_name='Агенство', default='Не указано')

    count_rooms = models.ForeignKey('CountRooms', on_delete=models.CASCADE, verbose_name='Количество комнат',
                                    default='Не указано')

    segment = models.ForeignKey('Segment', on_delete=models.SET_DEFAULT, verbose_name='Сегмент', default='Не указано')

    count_floors = models.PositiveSmallIntegerField(verbose_name='Этажность дома')

    material = models.ForeignKey('Material', on_delete=models.SET_DEFAULT, verbose_name='Материал', default='Не указано')

    floor = models.PositiveSmallIntegerField(verbose_name='Этаж', default=0)
    square_footage = models.FloatField(verbose_name='Площадь квартиры', default=0)
    square_footage_kitchen = models.FloatField(verbose_name='Площадь кухни, кв.м', default=0)

    have_balcony = models.ForeignKey('HaveBalcony', on_delete=models.SET_DEFAULT, verbose_name='Наличие балкона/лоджии',
                                     default='Не указано')

    how_long_from_metro = models.IntegerField(default=0, verbose_name='Удаленность от станции метро, мин')

    conditions = models.ForeignKey('Conditions', on_delete=models.SET_DEFAULT, verbose_name='Состояние',
                                  default='Не указано')

    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Все объявления'

    def __str__(self):
        return self.title
