# Generated by Django 5.1.7 on 2025-03-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_current_cycles_used_trip_current_cycle_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
