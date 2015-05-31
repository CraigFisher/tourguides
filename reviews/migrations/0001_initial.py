# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('rating', models.DecimalField(choices=[(0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], max_digits=2, decimal_places=1)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('guide', models.ForeignKey(to='profiles.GuideProfile')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GuideReviewDeletionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('reason', models.CharField(max_length=400)),
                ('requester', models.ForeignKey(to='profiles.GuideProfile')),
                ('review', models.ForeignKey(to='reviews.GuideReview')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TourReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('rating', models.DecimalField(choices=[(0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], max_digits=2, decimal_places=1)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(to='tours.Tour')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TourReviewDeletionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('reason', models.CharField(max_length=400)),
                ('requester', models.ForeignKey(to='profiles.GuideProfile')),
                ('review', models.ForeignKey(to='reviews.TourReview')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
