# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.TextField()),
                ('fecha_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
                ('idProducto', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
