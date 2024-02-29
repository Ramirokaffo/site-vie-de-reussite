# Generated by Django 4.2.9 on 2024-02-05 14:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0004_alter_ebookmodel_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebookmodel',
            name='description',
            field=tinymce.models.HTMLField(max_length=200000, verbose_name='description du livre'),
        ),
    ]
