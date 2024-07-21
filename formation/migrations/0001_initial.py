# Generated by Django 4.2.9 on 2024-07-21 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="Date d'ajout")),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('subtitle', models.CharField(default='', max_length=255, verbose_name='Texte présentatif')),
                ('description', tinymce.models.HTMLField(max_length=5000000, verbose_name='description de la formation')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('published', models.BooleanField(default=True, verbose_name='Publié')),
                ('illustration_image', models.ImageField(upload_to='images/formation/%Y/%m/%d', verbose_name="Image d'illustration")),
                ('illustration_video', models.CharField(blank=True, max_length=20, null=True, verbose_name="Identifiant de la vidéo d'illustration")),
                ('normal_price', models.FloatField(verbose_name='Prix barré')),
                ('promo_price', models.FloatField(verbose_name='Prix de vente')),
                ('course_duration', models.IntegerField(verbose_name='Durée totale des cours (en heures)')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categorymodel', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Formation',
                'verbose_name_plural': 'Formations',
            },
        ),
        migrations.CreateModel(
            name='FormationVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(auto_created=True, default=1, help_text="Ordre d'affichage de la vidéo", verbose_name='Ordre')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="Date d'ajout")),
                ('title', models.CharField(max_length=255, verbose_name='Titre de la vidéo')),
                ('decription', tinymce.models.HTMLField(blank=True, null=True)),
                ('video', models.CharField(blank=True, max_length=20, null=True, verbose_name='Identifiant de la vidéo')),
                ('published', models.BooleanField(default=True, verbose_name='Publié')),
                ('formation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formation.formation', verbose_name='Formation')),
            ],
            options={
                'verbose_name': 'Vidéo de formation',
                'verbose_name_plural': 'Vidéos de formation',
            },
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('content', models.TextField(max_length=200, verbose_name='Contenu')),
                ('published', models.BooleanField(default=True, verbose_name='Publié')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
                ('replies', models.ManyToManyField(blank=True, related_name='responses', to='formation.videocomment')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='formation.formationvideo', verbose_name='Vidéo')),
            ],
            options={
                'verbose_name': 'commentaire de vidéo',
                'verbose_name_plural': 'commentaires de vidéo',
            },
        ),
        migrations.CreateModel(
            name='SaleFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="date d'achat")),
                ('isPaid', models.BooleanField(default=False, verbose_name='payé ?')),
                ('amount', models.FloatField(verbose_name='montant facturé')),
                ('my_reference', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='reference de la transaction')),
                ('notch_pay_reference', models.CharField(blank=True, max_length=255, null=True, verbose_name='reference de notchpay')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='status du paiement')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour')),
                ('formation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formation.formation', verbose_name='formation achetée')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='acheté par')),
            ],
            options={
                'verbose_name': 'formation achetée',
                'verbose_name_plural': 'formations achetées',
            },
        ),
        migrations.CreateModel(
            name='PhysicFormationCmd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='date de commande')),
                ('isPaid', models.BooleanField(default=False, verbose_name='payé?')),
                ('amount', models.FloatField(verbose_name='montant facturé')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Téléphone client')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour')),
                ('formation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formation.formation', verbose_name='formation achetée')),
            ],
            options={
                'verbose_name': 'commande physique',
                'verbose_name_plural': 'commandes physiques',
            },
        ),
    ]
