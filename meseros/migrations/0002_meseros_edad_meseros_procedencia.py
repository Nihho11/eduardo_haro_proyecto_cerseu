# Generated by Django 4.2.1 on 2023-06-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meseros',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meseros',
            name='procedencia',
            field=models.CharField(default='Perú', max_length=30),
        ),
    ]
