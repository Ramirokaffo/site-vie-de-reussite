# Generated by Django 4.2.9 on 2024-02-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name="Date d'ajout")),
                ('full_name', models.CharField(max_length=255, verbose_name="nom complet de l'utilisateur")),
                ('phone_number', models.CharField(default='', max_length=255, verbose_name='numéro de téléphone')),
                ('objectif', models.TextField(verbose_name='onjectif de la réunion')),
                ('country', models.CharField(max_length=255, null=True, verbose_name='pays')),
                ('city', models.CharField(max_length=255, null=True, verbose_name='ville')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='email')),
                ('gender', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('A', 'Aucun')], default='H', max_length=2, null=True, verbose_name='sexe')),
                ('my_date', models.DateField(null=True, verbose_name='date du rendez')),
            ],
            options={
                'verbose_name': 'rendez-vous',
            },
        ),
    ]
