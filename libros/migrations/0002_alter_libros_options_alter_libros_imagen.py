# Generated by Django 4.1.3 on 2022-12-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libros',
            options={'verbose_name': 'libro', 'verbose_name_plural': 'libros'},
        ),
        migrations.AlterField(
            model_name='libros',
            name='imagen',
            field=models.ImageField(upload_to='libros'),
        ),
    ]
