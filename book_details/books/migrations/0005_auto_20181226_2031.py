# Generated by Django 2.0 on 2018-12-26 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20181226_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subgenre',
            old_name='genre',
            new_name='genre_name',
        ),
    ]
