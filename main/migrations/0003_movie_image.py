# Generated by Django 3.0.2 on 2020-02-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
