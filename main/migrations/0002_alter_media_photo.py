# Generated by Django 3.2.8 on 2021-11-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='изображение'),
        ),
    ]
