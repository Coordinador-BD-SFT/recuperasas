# Generated by Django 5.1 on 2024-08-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0011_reporte_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
