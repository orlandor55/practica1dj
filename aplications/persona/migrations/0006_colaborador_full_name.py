# Generated by Django 3.2.9 on 2021-11-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_auto_20211104_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='full_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombre'),
        ),
    ]
