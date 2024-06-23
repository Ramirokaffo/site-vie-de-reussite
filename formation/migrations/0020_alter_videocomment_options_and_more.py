# Generated by Django 4.2.9 on 2024-06-23 05:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0019_remove_formationvideo_last_updated_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videocomment',
            options={'verbose_name': 'commentaire de vidéo', 'verbose_name_plural': 'commentaires de vidéo'},
        ),
        migrations.AddField(
            model_name='saleformation',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour'),
        ),
        migrations.AddField(
            model_name='saleformation',
            name='my_reference',
            field=models.CharField(default=uuid.uuid4, max_length=255, verbose_name='reference de la transaction'),
        ),
        migrations.AddField(
            model_name='saleformation',
            name='notch_pay_reference',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='reference de notchpay'),
        ),
        migrations.AddField(
            model_name='saleformation',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='le status du paiement'),
        ),
    ]
