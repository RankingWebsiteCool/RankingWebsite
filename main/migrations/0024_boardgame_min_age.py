# Generated by Django 3.0.2 on 2020-07-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_boardgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='min_age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]