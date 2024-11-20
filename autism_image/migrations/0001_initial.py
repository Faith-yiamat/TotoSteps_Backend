# Generated by Django 4.2.16 on 2024-09-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autism_Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_upload', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]