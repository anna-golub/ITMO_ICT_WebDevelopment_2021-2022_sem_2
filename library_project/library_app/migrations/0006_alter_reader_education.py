# Generated by Django 4.0.4 on 2022-05-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_auto_20211208_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='education',
            field=models.CharField(blank=True, choices=[('Среднее общее', 'Среднее общее'), ('Среднее специальное', 'Среднее специальное'), ('Высшее', 'Высшее'), ('Неполное высшее', 'Неполное высшее'), ('Неполное среднее', 'Неполное среднее')], default='-', max_length=500, null=True, verbose_name='Образование'),
        ),
    ]