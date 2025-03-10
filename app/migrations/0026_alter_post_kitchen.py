# Generated by Django 4.2.19 on 2025-03-02 16:37

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0025_alter_post_add_bt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="kitchen",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("システムキッチン", "システムキッチン"),
                    ("カウンターキッチン", "カウンターキッチン"),
                    ("独立キッチン", "独立キッチン"),
                    ("L字キッチン", "L字キッチン"),
                ],
                default=[],
                max_length=32,
                verbose_name="キッチン",
            ),
        ),
    ]
