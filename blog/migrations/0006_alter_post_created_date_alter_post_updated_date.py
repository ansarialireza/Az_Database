# Generated by Django 5.0.4 on 2024-05-04 15:47

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
    ]