# Generated by Django 4.2.4 on 2024-08-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('broker', '0002_delete_userprofile_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userbroker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
