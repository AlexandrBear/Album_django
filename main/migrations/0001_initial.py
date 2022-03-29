# Generated by Django 3.2.8 on 2021-11-14 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Без названия', max_length=255, verbose_name='Название')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['time_create', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='изображение')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/%Y/%m/%d', verbose_name='Видео')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albums', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Медиа',
                'verbose_name_plural': 'Медиа',
                'ordering': ['id'],
            },
        ),
    ]
