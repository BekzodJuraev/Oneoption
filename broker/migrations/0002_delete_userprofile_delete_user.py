# Generated by Django 4.2.4 on 2024-08-27 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
