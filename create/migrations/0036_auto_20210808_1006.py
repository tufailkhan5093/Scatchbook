# Generated by Django 2.2.13 on 2021-08-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0035_auto_20210808_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2',
            name='lastname',
            field=models.CharField(default='Rithii', max_length=20),
        ),
    ]
