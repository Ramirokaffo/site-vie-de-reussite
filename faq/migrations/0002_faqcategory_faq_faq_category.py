# Generated by Django 4.2.9 on 2024-01-17 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='faq',
            name='faq_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='faq.faqcategory'),
        ),
    ]
