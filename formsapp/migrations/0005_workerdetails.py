# Generated by Django 5.0.6 on 2024-07-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0004_workerarea_alter_users_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Worker_image', models.ImageField(upload_to='images')),
                ('Contact_number', models.IntegerField()),
                ('Location', models.CharField(max_length=100)),
                ('Experience', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Reg_date', models.DateField(auto_now_add=True)),
                ('Accept', models.BooleanField(default=False)),
                ('Working_areas', models.ManyToManyField(to='formsapp.workerarea')),
            ],
        ),
    ]
