# Generated by Django 3.0.2 on 2020-02-29 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('released', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0), null=True)),
                ('released_order', models.PositiveIntegerField(null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('image', models.TextField(null=True)),
                ('certificate', models.CharField(max_length=10, null=True)),
                ('plot', models.TextField(null=True)),
                ('director', models.CharField(max_length=30, null=True)),
                ('language', models.CharField(max_length=10, null=True)),
                ('combined_ranking_order', models.PositiveIntegerField(null=True)),
                ('combined_ranking', models.FloatField(null=True)),
                ('runtime', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]