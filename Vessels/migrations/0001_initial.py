# Generated by Django 4.1.5 on 2023-04-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VesselSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voyage_number', models.CharField(max_length=50)),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Vessels.vessel')),
            ],
        ),
        migrations.CreateModel(
            name='PortCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=200)),
                ('port_country', models.CharField(max_length=2)),
                ('arrival', models.DateTimeField()),
                ('departure', models.DateTimeField()),
                ('vessel_schedule', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Vessels.vesselschedule')),
            ],
        ),
    ]
