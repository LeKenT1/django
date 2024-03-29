# Generated by Django 5.0.2 on 2024-02-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_planner', '0007_reservation_hebergement_alter_reservation_voyage'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='ville_arrivee',
            field=models.CharField(default='Ville par defaut', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyage',
            name='ville_depart',
            field=models.CharField(default='Ville par default', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voyage',
            name='lieu_arrivee',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='lieu_depart',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='mode_transport',
            field=models.CharField(choices=[('TR', 'Train'), ('AV', 'Avion'), ('VO', 'Voiture')], max_length=2),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='titre',
            field=models.CharField(max_length=100),
        ),
    ]
