# Generated by Django 4.2.19 on 2025-02-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_room_function_conro_num"),
    ]

    operations = [
        migrations.AddField(
            model_name="room_function",
            name="date",
            field=models.DateField(auto_now=True),
        ),
    ]
