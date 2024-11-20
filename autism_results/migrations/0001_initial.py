# Generated by Django 4.2.16 on 2024-09-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autism_image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autism_Results',
            fields=[
                ('results_id', models.AutoField(primary_key=True, serialize=False)),
                ('result', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autism_image.autism_image')),
            ],
        ),
    ]
