# Generated by Django 4.2.9 on 2024-02-03 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categorymodel_options_categorymodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': "Catégorie d'élément", 'verbose_name_plural': "Catégories d'éléments"},
        ),
    ]
