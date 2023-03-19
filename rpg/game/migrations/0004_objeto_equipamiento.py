# Generated by Django 4.1.7 on 2023-03-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_personaje_dinero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('personaje', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Equipamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('personaje', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.personaje')),
            ],
        ),
    ]
