# Generated by Django 2.2.13 on 2021-08-08 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0023_auto_20210808_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2',
            name='firstname',
            field=models.CharField(blank=True, default='boob', max_length=20),
        ),
    ]