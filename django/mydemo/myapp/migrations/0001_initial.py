# Generated by Django 4.2.9 on 2024-01-18 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                # ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32)),
                ("age", models.IntegerField(default=20)),
                ("phone", models.CharField(max_length=16)),
                ("addtime", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
