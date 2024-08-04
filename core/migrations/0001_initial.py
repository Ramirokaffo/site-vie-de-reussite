# Generated by Django 4.2.9 on 2024-08-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='Nom')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': "Catégorie d'élément",
                'verbose_name_plural': "Catégories d'éléments",
            },
        ),
        migrations.CreateModel(
            name='SiteVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=255, null=True, unique=True, verbose_name='titre de la vidéo')),
                ('video', models.CharField(max_length=255, null=True, unique=True, verbose_name='identifiant YouTube de la vidéo')),
                ('show_where', models.CharField(choices=[('home', 'Accueil'), ('formations', 'Formations'), ('formation', 'Détails des formations'), ('ebooks', 'Ebooks'), ('ebook', 'Détails des ebooks'), ('events', 'Évènements'), ('event', 'Détail des évènements'), ('faq', 'Foire aux questions'), ('about', 'À propos'), ('blog', 'Blog'), ('post', 'Post')], default='home', max_length=15, verbose_name='Afficher où ?')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True, verbose_name='Publié')),
            ],
            options={
                'verbose_name': 'vidéo du site',
                'verbose_name_plural': 'vidéos du site',
            },
        ),
    ]
