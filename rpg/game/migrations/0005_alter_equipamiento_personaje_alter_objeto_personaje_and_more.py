# Generated by Django 4.1.7 on 2023-03-18 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_objeto_equipamiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamiento',
            name='personaje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipamiento', to='game.personaje'),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='personaje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objeto', to='game.personaje'),
        ),
        migrations.CreateModel(
            name='Caballo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('inventario', models.IntegerField()),
                ('personaje', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caballo', to='game.personaje')),
            ],
        ),
    ]
