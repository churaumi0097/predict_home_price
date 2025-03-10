# Generated by Django 4.2.19 on 2025-03-02 16:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0026_alter_post_kitchen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="add_bt",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("追焚機能", "追焚機能"),
                    ("浴室乾燥機", "浴室乾燥機"),
                    ("温水洗浄便座", "温水洗浄便座"),
                    ("脱衣所", "脱衣所"),
                ],
                default=[],
                max_length=21,
                verbose_name="バストイレ追加機能",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="conro",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[("ガスコンロ", "ガスコンロ"), ("電気コンロ", "電気コンロ"), ("IHコンロ", "IHコンロ")],
                default=[],
                max_length=17,
                verbose_name="コンロ",
            ),
        ),
    ]
