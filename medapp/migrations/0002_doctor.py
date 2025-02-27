# Generated by Django 5.1.6 on 2025-02-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
            ],
        ),
    ]
