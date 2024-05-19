# Generated by Django 4.2.9 on 2024-05-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0016_formationvideo_order_alter_formationvideo_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleformation',
            options={'verbose_name': 'formation commandée', 'verbose_name_plural': 'formations commandées'},
        ),
        migrations.AlterField(
            model_name='formationvideo',
            name='order',
            field=models.IntegerField(auto_created=True, default=1, help_text="Ordre d'affichage de la vidéo", verbose_name='Ordre'),
        ),
    ]
