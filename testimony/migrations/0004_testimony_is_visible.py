# Generated by Django 4.2.9 on 2024-02-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimony', '0003_alter_testimony_content_alter_testimony_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
