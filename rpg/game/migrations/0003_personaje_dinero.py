# Generated by Django 4.1.7 on 2023-03-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_personaje_natletismo_personaje_ncraft_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaje',
            name='dinero',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
    ]
