# Generated by Django 3.0.2 on 2020-07-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_videogame_videogamecsvdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videogame',
            old_name='min_completion_time',
            new_name='runtime',
        ),
    ]
