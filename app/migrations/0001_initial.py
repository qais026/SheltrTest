# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('admin_firstname2', models.CharField(null=True, max_length=45, blank=True)),
                ('admin_lastname2', models.CharField(null=True, max_length=45, blank=True)),
                ('name', models.CharField(max_length=140)),
                ('logo', models.CharField(null=True, max_length=140, blank=True)),
                ('URL', models.CharField(max_length=140)),
                ('street', models.CharField(max_length=140)),
                ('city', models.CharField(max_length=60)),
                ('zipcode', models.CharField(max_length=10)),
                ('latitude', models.FloatField(null=True, default=0, blank=True)),
                ('longitude', models.FloatField(null=True, default=0, blank=True)),
                ('characteristics', models.CharField(max_length=500)),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
