# Generated by Django 2.2.13 on 2021-08-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0021_auto_20210808_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2',
            name='lastname',
            field=models.CharField(default='Khan', max_length=20),
        ),
    ]
