# Generated by Django 4.2.9 on 2024-07-21 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ebook.models
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
            name='EbookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="Date d'ajout")),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='titre du livre')),
                ('subtitle', models.CharField(default='', max_length=255, verbose_name='Texte présentatif')),
                ('description', tinymce.models.HTMLField(max_length=5000000, verbose_name='description du livre')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour')),
                ('ebook_file', models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', validators=[ebook.models.validate_pdf_file], verbose_name='Livre au format pdf')),
                ('illustration_image', models.ImageField(blank=True, null=True, upload_to='images/ebook/%Y/%m/%d', verbose_name="Image d'illustration")),
                ('illustration_video', models.CharField(blank=True, max_length=20, null=True, verbose_name="identifiant vers la vidéo d'illustration")),
                ('normal_price', models.FloatField(verbose_name='prix barré')),
                ('promo_price', models.FloatField(verbose_name='prix de vente/facturé')),
                ('published', models.BooleanField(default=True, verbose_name='publié')),
                ('availability', models.CharField(choices=[('numeric', 'Uniquement la version physique'), ('physic', 'Uniquement la version numérique'), ('both', 'Version physique et numerique disponibles')], default='both', max_length=10, verbose_name='version disponible')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categorymodel', verbose_name='Catégorie du livre')),
            ],
            options={
                'verbose_name': 'e-book',
                'verbose_name_plural': 'e-books',
            },
        ),
        migrations.CreateModel(
            name='SaleEbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="date d'achat")),
                ('isPaid', models.BooleanField(default=False, verbose_name='payé ?')),
                ('amount', models.FloatField(verbose_name='montant facturé')),
                ('my_reference', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='reference de la transaction')),
                ('notch_pay_reference', models.CharField(blank=True, max_length=255, null=True, verbose_name='reference de notchpay')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='le status du paiement')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour')),
                ('buy_version', models.CharField(choices=[('numeric', 'Uniquement la version physique'), ('physic', 'Uniquement la version numérique')], default='numeric', max_length=10, verbose_name='version achetée')),
                ('ebook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ebook.ebookmodel', verbose_name='livre acheté')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='acheté par')),
            ],
            options={
                'verbose_name': 'livre vendu',
                'verbose_name_plural': 'livres vendus',
            },
        ),
        migrations.CreateModel(
            name='PhysicEbookCmd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='date de commande')),
                ('isPaid', models.BooleanField(default=False, verbose_name='payé ?')),
                ('amount', models.FloatField(verbose_name='montant facturé')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Téléphone client')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour')),
                ('ebook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ebook.ebookmodel', verbose_name='livre acheté')),
            ],
            options={
                'verbose_name': 'commande physique',
                'verbose_name_plural': 'commandes physiques',
            },
        ),
    ]
