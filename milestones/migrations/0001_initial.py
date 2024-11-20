# Generated by Django 4.2.16 on 2024-09-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('milestone_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(choices=[(2, '2 Months'), (4, '4 Months'), (6, '6 Months'), (9, '9 Months'), (12, '12 Months'), (15, '15 Months'), (18, '18 Months'), (24, '24 Months'), (30, '30 Months'), (36, '36 Months')])),
                ('category', models.CharField(choices=[('Social', 'Social'), ('Language', 'Language'), ('Cognitive', 'Cognitive'), ('Movement', 'Movement')], max_length=50)),
                ('summary', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_current', models.BooleanField(default=False)),
                ('child_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.child')),
            ],
        ),
    ]
