# Generated by Django 4.1.8 on 2023-04-07 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rest_framework_api_key", "0005_auto_20220110_1102"),
        ("indexes", "0002_remove_document_uploaded_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="collection",
            name="author",
        ),
        migrations.AddField(
            model_name="collection",
            name="api_key",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rest_framework_api_key.apikey",
            ),
        ),
    ]
