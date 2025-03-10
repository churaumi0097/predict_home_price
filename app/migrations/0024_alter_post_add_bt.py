# Generated by Django 4.2.19 on 2025-03-02 16:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0023_alter_post_add_bt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="add_bt",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[("浴室乾燥機", "浴室乾燥機"), ("脱衣所", "脱衣所"), ("追焚機能", "追焚機能")],
                default=[],
                max_length=14,
                verbose_name="バストイレ追加機能",
            ),
        ),
    ]
