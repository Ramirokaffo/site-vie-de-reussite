# Generated by Django 4.2.9 on 2024-02-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0008_faq_category_alter_faq_answer_alter_faq_faq_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='category',
            field=models.CharField(choices=[('formation', 'Formation'), ('ebook', 'Livres'), ('about', "À propos de l'activité")], max_length=20, verbose_name='Catégorie de Faq'),
        ),
    ]
