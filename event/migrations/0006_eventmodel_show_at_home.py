# Generated by Django 4.2.9 on 2024-05-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_eventmodel_inscription_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='show_at_home',
            field=models.BooleanField(default=False, verbose_name="afficher à l'accueil"),
        ),
    ]
