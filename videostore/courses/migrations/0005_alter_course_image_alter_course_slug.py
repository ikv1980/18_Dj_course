# Generated by Django 4.0.5 on 2022-07-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_lesson_options_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.png', upload_to='course_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Уникальное название курса'),
        ),
    ]
