# Generated by Django 2.2.13 on 2021-08-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0030_auto_20210808_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2',
            name='cover_pic',
            field=models.ImageField(default=False, upload_to='coverpic'),
        ),
    ]
