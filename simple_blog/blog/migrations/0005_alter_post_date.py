# Generated by Django 4.2.6 on 2024-02-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
