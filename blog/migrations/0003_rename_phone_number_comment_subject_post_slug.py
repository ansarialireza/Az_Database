# Generated by Django 5.0.4 on 2024-05-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_subject_comment_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='phone_number',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
