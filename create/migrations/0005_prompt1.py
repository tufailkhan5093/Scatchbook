# Generated by Django 2.2.13 on 2021-08-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0004_message2'),
    ]

    operations = [
        migrations.CreateModel(
            name='prompt1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=255)),
            ],
        ),
    ]