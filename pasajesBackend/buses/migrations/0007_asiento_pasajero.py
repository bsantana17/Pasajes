# Generated by Django 2.1.5 on 2019-01-23 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('buses', '0006_auto_20190123_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='asiento',
            name='pasajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
    ]