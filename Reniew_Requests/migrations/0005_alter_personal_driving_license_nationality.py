# Generated by Django 5.0.3 on 2024-05-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reniew_Requests', '0004_alter_personal_driving_license_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_driving_license',
            name='Nationality',
            field=models.CharField(choices=[('Egyptian', 'Egyptian')], max_length=255),
        ),
    ]
