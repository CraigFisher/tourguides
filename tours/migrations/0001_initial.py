# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20150420_1455'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=300)),
                ('overview', models.TextField(null=True)),
                ('itinerary', models.TextField(null=True)),
                ('max_seating', models.SmallIntegerField(default=1)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('city', models.ForeignKey(null=True, to='cities_light.City')),
                ('country', models.ForeignKey(to='cities_light.Country')),
                ('region', models.ForeignKey(null=True, to='cities_light.Region')),
                ('tour_guide', models.ForeignKey(to='profiles.GuideProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
