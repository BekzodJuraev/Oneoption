# Generated by Django 4.2.4 on 2024-10-10 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_remove_ftd_profile_ftd_user_broker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_by_ref',
            name='profile',
        ),
    ]