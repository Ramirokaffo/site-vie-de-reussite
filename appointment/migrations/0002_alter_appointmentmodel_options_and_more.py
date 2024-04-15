# Generated by Django 4.2.9 on 2024-03-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointmentmodel',
            options={'verbose_name': 'rendez-vous', 'verbose_name_plural': 'rendez-vous'},
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="date d'ajout"),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='nom complet'),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='my_date',
            field=models.DateField(null=True, verbose_name='date du rendez-vous'),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='phone_number',
            field=models.CharField(default='', max_length=255, verbose_name='téléphone'),
        ),
    ]
