# Generated by Django 5.0.3 on 2024-05-04 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_state',
            name='Blood_quarter',
            field=models.CharField(choices=[('A+', 'A Plus'), ('A-', 'A Minus'), ('B+', 'B Plus'), ('B-', 'B Minus'), ('AB+', 'Ab Plus'), ('AB-', 'Ab Minus'), ('O+', 'O Plus'), ('O-', 'O Minus')], default=None, max_length=3),
        ),
    ]
