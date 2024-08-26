# Generated by Django 5.0.6 on 2024-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
