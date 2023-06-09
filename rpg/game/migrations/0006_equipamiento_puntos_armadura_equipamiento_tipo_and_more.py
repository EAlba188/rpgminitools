# Generated by Django 4.1.7 on 2023-03-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_equipamiento_personaje_alter_objeto_personaje_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamiento',
            name='puntos_armadura',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='tipo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='dinero',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=19),
        ),
    ]
