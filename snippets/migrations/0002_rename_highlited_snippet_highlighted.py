# Generated by Django 3.2.4 on 2021-06-24 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='highlited',
            new_name='highlighted',
        ),
    ]
