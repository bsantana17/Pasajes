# Generated by Django 2.1.5 on 2019-01-26 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0009_auto_20190123_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='buses',
        ),
        migrations.AddField(
            model_name='bus',
            name='horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='buses.Horario'),
        ),
        migrations.AlterField(
            model_name='asiento',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.Bus'),
        ),
        migrations.AlterField(
            model_name='asiento',
            name='pasajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='chofer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.Usuario'),
        ),
    ]