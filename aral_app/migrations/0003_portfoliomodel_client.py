# Generated by Django 5.0.4 on 2024-04-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aral_app', '0002_ourpartnersmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='client',
            field=models.CharField(default='', max_length=100),
        ),
    ]
