# Generated by Django 2.2.13 on 2021-08-08 05:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0038_auto_20210808_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step3',
            name='first',
            field=ckeditor.fields.RichTextField(default='Mehak'),
        ),
    ]