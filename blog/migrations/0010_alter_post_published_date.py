# Generated by Django 5.0.4 on 2024-05-04 16:27

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ انتشار'),
        ),
    ]