# Generated by Django 5.0.2 on 2024-02-29 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_planner', '0006_hebergement'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hebergement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_planner.hebergement'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='voyage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_planner.voyage'),
        ),
    ]