# Generated by Django 4.1.7 on 2023-03-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaje',
            name='natletismo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='ncraft',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='ndestreza',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='nfuerza',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='ninteligencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='npercepcion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='npersuasion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaje',
            name='nsigilo',
            field=models.IntegerField(default=0),
        ),
    ]