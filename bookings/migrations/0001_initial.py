# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('number_guests', models.SmallIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('req', 'REQUESTED'), ('conf', 'CONFIRMED'), ('prog', 'IN_PROGRESS'), ('fin', 'FINISHED'), ('canc', 'CANCELLED')], max_length=4, default='R')),
                ('request_time', models.DateTimeField()),
                ('cancelation_time', models.DateTimeField(null=True)),
                ('confirmation_time', models.DateTimeField(null=True)),
                ('member', models.ForeignKey(to='profiles.MemberProfile')),
                ('tour', models.ForeignKey(to='tours.Tour')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
