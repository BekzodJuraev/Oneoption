# Generated by Django 4.1.2 on 2024-07-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_remove_referral_click_count_click_referral'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='balance',
            new_name='deposit',
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]