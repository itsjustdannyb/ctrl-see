# Generated by Django 5.1.2 on 2024-12-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_textdocument_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textdocument",
            name="title",
            field=models.CharField(max_length=200, unique=True, verbose_name="Title"),
        ),
    ]
