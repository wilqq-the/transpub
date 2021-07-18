# Generated by Django 3.2.5 on 2021-07-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('veh_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('gmvid', models.SmallIntegerField()),
                ('linia', models.TextField()),
                ('kierunek', models.TextField()),
                ('z', models.TextField()),
                ('w_kierunku', models.TextField()),
                ('lat', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('lon', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('opoznienie', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('time_stamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'buses',
                'managed': False,
            },
        ),
    ]