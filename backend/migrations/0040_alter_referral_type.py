# Generated by Django 4.2.4 on 2024-10-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0039_alter_referral_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='type',
            field=models.CharField(choices=[('main', 'Главная страница '), ('register', ' Ссылка на регистрацию'), ('fast', ' Быстрый вход в платформу')], max_length=20),
        ),
    ]
