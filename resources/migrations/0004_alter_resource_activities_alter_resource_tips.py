# Generated by Django 4.2.16 on 2024-10-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0003_alter_resource_activities_alter_resource_tips"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="activities",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="resource",
            name="tips",
            field=models.JSONField(),
        ),
    ]
