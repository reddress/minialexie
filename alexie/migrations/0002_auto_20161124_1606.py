# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alexie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AccountUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AccountTypeUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TransactionUser', to=settings.AUTH_USER_MODEL),
        ),
    ]