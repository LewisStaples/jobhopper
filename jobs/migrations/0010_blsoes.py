# Generated by Django 3.1 on 2020-10-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20201013_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlsOes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('area_title', models.CharField(max_length=255, null=True)),
                ('soc_code', models.CharField(max_length=10, null=True)),
                ('soc_title', models.CharField(max_length=255, null=True)),
                ('hourly_mean_wage', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('annual_mean_wage', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_employment', models.BigIntegerField(null=True)),
                ('soc_decimal_code', models.CharField(max_length=10, null=True)),
            ],
        )
    ]