# Generated by Django 3.0.2 on 2020-02-29 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('released', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0), verbose_name='date published')),
                ('released_order', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=30)),
                ('certificate', models.CharField(max_length=10)),
                ('plot', models.TextField()),
                ('director', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=10)),
                ('combined_ranking_order', models.PositiveIntegerField()),
                ('combined_ranking', models.FloatField()),
                ('runtime', models.PositiveIntegerField()),
            ],
        ),
    ]
