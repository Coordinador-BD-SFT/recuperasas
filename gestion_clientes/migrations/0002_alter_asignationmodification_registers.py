# Generated by Django 5.1.1 on 2024-09-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignationmodification',
            name='registers',
            field=models.IntegerField(default=0),
        ),
    ]
