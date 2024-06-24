# Generated by Django 4.1.2 on 2024-05-14 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theatre_side', '0003_theatre_delete_theater'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimePasswordTheatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('theatre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='theatre_side.theatre')),
            ],
        ),
    ]