# Generated by Django 4.1.2 on 2024-10-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_register_by_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='recommended_by',
        ),
    ]