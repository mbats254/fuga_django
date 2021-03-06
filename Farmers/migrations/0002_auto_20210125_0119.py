# Generated by Django 3.0.5 on 2021-01-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('breed', models.CharField(max_length=64)),
                ('uniqid', models.CharField(default='uniqid_unset', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('uniqid', models.CharField(default='uniqid_unset', max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='farmers',
            name='uniqid',
            field=models.CharField(default='uniqid_unset', max_length=12),
        ),
    ]
