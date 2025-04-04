# Generated by Django 5.1.7 on 2025-03-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_location', models.JSONField()),
                ('cycles_used', models.IntegerField()),
                ('pick_up_location', models.JSONField()),
                ('drop_off_location', models.JSONField()),
            ],
        ),
    ]
