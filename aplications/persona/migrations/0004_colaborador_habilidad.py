# Generated by Django 3.2.9 on 2021-11-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='habilidad',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
