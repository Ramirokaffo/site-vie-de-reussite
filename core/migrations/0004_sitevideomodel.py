# Generated by Django 4.2.9 on 2024-04-07 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, unique=True, verbose_name='titre')),
                ('video', models.CharField(max_length=255, null=True, unique=True, verbose_name='identifiant de la vidéo')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('published', models.BooleanField(default=True, verbose_name='Publié')),
            ],
            options={
                'verbose_name': 'vidéo du site',
                'verbose_name_plural': 'vidéos du site',
            },
        ),
    ]
