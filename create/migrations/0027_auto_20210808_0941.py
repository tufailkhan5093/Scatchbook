# Generated by Django 2.2.13 on 2021-08-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0026_auto_20210808_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='step2',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]