# Generated by Django 3.0.5 on 2021-01-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmers', '0003_auto_20210125_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='uniqid',
            field=models.CharField(default='uniqid_unset', max_length=12),
        ),
    ]
