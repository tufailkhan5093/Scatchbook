# Generated by Django 2.2.13 on 2021-08-02 15:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step3',
            name='first',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='step3',
            name='second',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='step3',
            name='third',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
