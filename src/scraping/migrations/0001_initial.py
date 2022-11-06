# Generated by Django 3.0.14 on 2022-11-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название района')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Название района',
                'verbose_name_plural': 'Название районов',
            },
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Состояние')),
                ('slug', models.CharField(blank=True, max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Состояние квартиры',
                'verbose_name_plural': 'Состояние квартир',
            },
        ),
        migrations.CreateModel(
            name='HaveBalcony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наличие балкона/лоджии')),
                ('slug', models.CharField(blank=True, max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Наличие балкона/лоджии',
                'verbose_name_plural': 'Наличие балкона/лоджии',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Материал')),
                ('slug', models.CharField(blank=True, max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Материал стен',
                'verbose_name_plural': 'Разновидность материалов стен',
            },
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Сегмент')),
                ('slug', models.CharField(blank=True, max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Вид сегмента',
                'verbose_name_plural': 'Все виды сегмента',
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок объявления')),
                ('address', models.CharField(max_length=250, verbose_name='Местоположение')),
                ('price', models.FloatField(default=0, verbose_name='Стоимость')),
                ('company', models.CharField(default='Не указано', max_length=250, verbose_name='Агенство')),
                ('count_rooms', models.CharField(default='Не указано', max_length=100, verbose_name='Количество комнат')),
                ('count_floors', models.PositiveSmallIntegerField(verbose_name='Этажность дома')),
                ('floor', models.PositiveSmallIntegerField(default=0, verbose_name='Этаж')),
                ('square_footage', models.FloatField(default=0, verbose_name='Площадь квартиры')),
                ('square_footage_kitchen', models.FloatField(default=0, verbose_name='Площадь кухни, кв.м')),
                ('how_long_from_metro', models.IntegerField(default=0, verbose_name='Удаленность от станции метро, мин')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(default='Не указано', on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='Район')),
                ('condition', models.ForeignKey(default='Не указано', on_delete=django.db.models.deletion.SET_DEFAULT, to='scraping.Conditions', verbose_name='Состояние')),
                ('have_balcony', models.ForeignKey(default='Не указано', on_delete=django.db.models.deletion.SET_DEFAULT, to='scraping.HaveBalcony', verbose_name='Наличие балкона/лоджии')),
                ('material', models.ForeignKey(default='Не указано', on_delete=django.db.models.deletion.SET_DEFAULT, to='scraping.Material')),
                ('segment', models.ForeignKey(default='Не указано', on_delete=django.db.models.deletion.SET_DEFAULT, to='scraping.Segment', verbose_name='Сегмент')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Все объявления',
            },
        ),
    ]
