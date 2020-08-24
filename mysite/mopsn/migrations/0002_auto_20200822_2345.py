# Generated by Django 3.1 on 2020-08-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mopsn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='netflix',
            name='lang',
        ),
        migrations.AddField(
            model_name='netflix',
            name='account_period',
            field=models.CharField(choices=[('3-M', 'Three_month'), ('6-M', 'Six_month'), ('12-M', 'Twelve_month')], default='3-M', max_length=4),
        ),
        migrations.AddField(
            model_name='netflix',
            name='language',
            field=models.CharField(blank=True, default='English', max_length=30, null=True),
        ),
    ]
