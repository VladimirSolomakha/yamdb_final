# Generated by Django 2.2.16 on 2022-08-19 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_merge_20220817_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',), 'verbose_name': 'Жанры'},
        ),
    ]
