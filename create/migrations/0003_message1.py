# Generated by Django 2.2.13 on 2021-08-07 17:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_auto_20210802_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='message1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
