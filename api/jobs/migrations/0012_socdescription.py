# Generated by Django 3.1 on 2020-10-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20201024_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('soc_code', models.CharField(max_length=10, null=True)),
                ('soc_title', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
