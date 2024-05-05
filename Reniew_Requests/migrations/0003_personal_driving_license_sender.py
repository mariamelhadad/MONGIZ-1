# Generated by Django 5.0.3 on 2024-05-04 22:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reniew_Requests', '0002_personal_id_card_sender'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_driving_license',
            name='Sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender_driving_license', to=settings.AUTH_USER_MODEL),
        ),
    ]
