# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_code', models.CharField(default='', max_length=32, verbose_name='Asset ID')),
                ('scan_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Scan Time')),
                ('d1', models.CharField(default='0.0', max_length=8)),
                ('d2', models.CharField(default='0.0', max_length=8)),
                ('d3', models.CharField(default='0.0', max_length=8)),
                ('h1', models.CharField(default='0.0', max_length=8)),
                ('h2', models.CharField(default='0.0', max_length=8)),
                ('h3', models.CharField(default='0.0', max_length=8)),
                ('cp', models.CharField(default='0.0', max_length=8)),
                ('fc', models.CharField(default='0.0', max_length=8)),
                ('location', models.CharField(default='', max_length=100, verbose_name='location')),
                ('product_details', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Product details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_code', models.CharField(default='', max_length=32, verbose_name='Asset ID')),
                ('scan_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Scan Time')),
                ('d1', models.CharField(default='0.0', max_length=8)),
                ('d2', models.CharField(default='0.0', max_length=8)),
                ('d3', models.CharField(default='0.0', max_length=8)),
                ('h1', models.CharField(default='0.0', max_length=8)),
                ('h2', models.CharField(default='0.0', max_length=8)),
                ('h3', models.CharField(default='0.0', max_length=8)),
                ('cp', models.CharField(default='0.0', max_length=8)),
                ('fc', models.CharField(default='0.0', max_length=8)),
                ('status', models.IntegerField(choices=[(1, 'Registered'), (2, 'Verified'), (3, 'Tampered'), (4, 'Tampered WLC')], verbose_name='Staus')),
                ('operator', models.CharField(default='', max_length=32, verbose_name='Operator')),
                ('geo_location', models.CharField(default='0.0|0.0', max_length=32, verbose_name='Geo Point')),
                ('street', models.CharField(default='', max_length=32, verbose_name='Address')),
                ('locality', models.CharField(default='', max_length=128, verbose_name='locality')),
                ('city', models.CharField(default='', max_length=32, verbose_name='city')),
                ('state', models.CharField(default='', max_length=32, verbose_name='state')),
                ('postal_code', models.CharField(default='', max_length=16, verbose_name='Postal Code')),
                ('country', models.CharField(default='', max_length=32, verbose_name='country')),
                ('mobile', models.CharField(default='', max_length=16, verbose_name='mobile')),
                ('scan_remark', models.CharField(default='Not Provided', max_length=100, verbose_name='Scan Remark')),
                ('bit_mask', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Bit Mask')),
                ('email_id', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Email Id')),
                ('image', models.FileField(upload_to='media/documents/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]