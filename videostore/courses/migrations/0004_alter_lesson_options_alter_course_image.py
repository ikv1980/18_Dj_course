# Generated by Django 4.0.6 on 2022-07-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Лекция', 'verbose_name_plural': 'Лекции'},
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.png', upload_to='course2_images', verbose_name='Изображение'),
        ),
    ]
