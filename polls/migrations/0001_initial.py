# Generated by Django 3.2.5 on 2023-04-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePageperformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_url', models.URLField(max_length=255)),
                ('mobile_data', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pageperformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_url', models.URLField(max_length=255)),
                ('output_data', models.TextField(max_length=255)),
            ],
        ),
    ]