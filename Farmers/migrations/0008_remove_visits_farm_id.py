# Generated by Django 3.0.5 on 2021-01-25 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Farmers', '0007_auto_20210125_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visits',
            name='farm_id',
        ),
    ]
