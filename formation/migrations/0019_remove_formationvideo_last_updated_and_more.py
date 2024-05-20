# Generated by Django 4.2.9 on 2024-05-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0018_formationvideo_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formationvideo',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='formation',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour'),
        ),
    ]