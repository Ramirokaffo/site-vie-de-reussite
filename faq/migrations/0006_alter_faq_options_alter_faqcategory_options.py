# Generated by Django 4.2.9 on 2024-01-31 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0005_alter_faq_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['-created_at'], 'verbose_name': 'Foire aux questions'},
        ),
        migrations.AlterModelOptions(
            name='faqcategory',
            options={'ordering': ['-created_at'], 'verbose_name': 'Catégorie de question', 'verbose_name_plural': 'Catégories de question'},
        ),
    ]
