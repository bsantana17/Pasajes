# Generated by Django 2.1.5 on 2019-01-26 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0013_auto_20190126_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asiento',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.Bus'),
        ),
        migrations.AlterField(
            model_name='asiento',
            name='pasajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.Usuario'),
        ),
    ]