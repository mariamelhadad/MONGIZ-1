# Generated by Django 5.0.3 on 2024-03-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='papers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bith_cirtification', models.ImageField(upload_to='')),
                ('Passport', models.ImageField(upload_to='')),
                ('Driving_Licence', models.ImageField(upload_to='')),
            ],
        ),
    ]
