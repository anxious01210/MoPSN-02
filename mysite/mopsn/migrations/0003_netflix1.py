# Generated by Django 3.1 on 2020-08-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mopsn', '0002_auto_20200822_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='mopsn/images')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
