# Generated by Django 4.2.9 on 2024-02-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimony', '0002_alter_testimony_options_alter_testimony_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='created_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Modifié le'),
        ),
    ]
