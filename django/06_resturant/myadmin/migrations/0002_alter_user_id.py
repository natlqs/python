# Generated by Django 4.2.9 on 2024-01-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myadmin", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]