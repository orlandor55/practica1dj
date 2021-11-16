# Generated by Django 3.2.9 on 2021-11-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_auto_20211108_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='colaborador'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='job',
            field=models.CharField(choices=[('contador', 'Contador'), ('administrador', 'Administrador'), ('economista', 'Economista'), ('otros', 'Otros')], max_length=50, verbose_name='Cargo'),
        ),
    ]
