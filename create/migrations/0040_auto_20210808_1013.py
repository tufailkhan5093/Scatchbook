# Generated by Django 2.2.13 on 2021-08-08 05:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0039_auto_20210808_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step3',
            name='second',
            field=ckeditor.fields.RichTextField(default='Mehak'),
        ),
        migrations.AlterField(
            model_name='step3',
            name='third',
            field=ckeditor.fields.RichTextField(default='Mehak'),
        ),
    ]
