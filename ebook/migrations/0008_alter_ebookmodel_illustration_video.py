# Generated by Django 4.2.9 on 2024-05-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0007_alter_ebookmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebookmodel',
            name='illustration_video',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name="Identifiant vers la vidéo d'illustration"),
        ),
    ]