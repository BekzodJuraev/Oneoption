# Generated by Django 4.1.2 on 2024-09-02 06:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0004_alter_userbroker_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbroker',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
