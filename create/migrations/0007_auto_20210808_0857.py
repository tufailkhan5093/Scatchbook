# Generated by Django 2.2.13 on 2021-08-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0006_prompt2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step2',
            name='cover_pic',
            field=models.ImageField(blank=True, upload_to='coverpic'),
        ),
        migrations.AlterField(
            model_name='step2',
            name='firstname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='step2',
            name='lastname',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]