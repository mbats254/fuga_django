# Generated by Django 3.0.5 on 2021-01-25 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Farmers', '0005_auto_20210125_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='farm_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='farm', to='Farmers.Farm'),
        ),
    ]
