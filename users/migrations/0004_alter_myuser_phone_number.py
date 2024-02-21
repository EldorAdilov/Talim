# Generated by Django 5.0.2 on 2024-02-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_myuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=100, unique=True, verbose_name='phone_number', null=True, blank=True),
        ),
    ]
