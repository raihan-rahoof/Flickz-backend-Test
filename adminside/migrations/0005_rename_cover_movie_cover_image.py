# Generated by Django 4.1.2 on 2024-05-24 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0004_movie_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='cover',
            new_name='cover_image',
        ),
    ]
