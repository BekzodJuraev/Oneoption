# Generated by Django 4.1.2 on 2024-07-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]
