# Generated by Django 4.2.9 on 2024-02-19 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0009_alter_faq_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='faq_category',
        ),
    ]
