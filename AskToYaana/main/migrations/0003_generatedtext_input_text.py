# Generated by Django 5.1 on 2024-08-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_generatedtext_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="generatedtext",
            name="input_text",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1 on 2024-08-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_generatedtext_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="generatedtext",
            name="input_text",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]