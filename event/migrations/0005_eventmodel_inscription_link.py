# Generated by Django 4.2.9 on 2024-05-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_eventmodel_illustration_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='inscription_link',
            field=models.CharField(blank=True, max_length=355, null=True, verbose_name="lien d'inscription"),
        ),
    ]
