# Generated by Django 2.1.5 on 2019-01-23 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('buses', '0007_asiento_pasajero'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='chofer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
    ]
