# Generated by Django 4.1.2 on 2024-07-03 13:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_passwordreset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('referral_type', models.CharField(choices=[('doxod', 'Doxod'), ('oborot', 'Oborot'), ('sub', 'Sub')], max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.profile')),
            ],
        ),
    ]
