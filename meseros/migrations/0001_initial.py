# Generated by Django 4.2.1 on 2023-05-19 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meseros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(default='Peruano', max_length=30)),
            ],
        ),
    ]
