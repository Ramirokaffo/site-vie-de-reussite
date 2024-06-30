# Generated by Django 4.2.9 on 2024-06-30 03:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='Date de publication')),
                ('first_name', models.CharField(max_length=255, verbose_name='nom')),
                ('last_name', models.CharField(max_length=255, verbose_name='prénom')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='email')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='dernière mise à jour')),
                ('is_subscrib', models.BooleanField(default=True, verbose_name='abonné(e)')),
            ],
            options={
                'verbose_name': 'abonné',
                'verbose_name_plural': 'abonnés',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SubscribersGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='Date de publication')),
                ('name', models.CharField(max_length=255, verbose_name='nom du groupe')),
                ('subscribers', models.ManyToManyField(to='newsletter.subscribers', verbose_name='abonné(e)')),
            ],
            options={
                'verbose_name': "groupe d'abonné",
                'verbose_name_plural': "groupes d'abonné",
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='Date de publication')),
                ('object', models.CharField(max_length=255, verbose_name='objet')),
                ('is_subscrib', models.BooleanField(default=True, verbose_name='abonné(e)')),
                ('content', tinymce.models.HTMLField(blank=True, max_length=5000000, verbose_name='message')),
                ('subscribers', models.ManyToManyField(blank=True, related_name='subscribers', to='newsletter.subscribers')),
                ('subscribers_group', models.ManyToManyField(blank=True, related_name='subscribers_group', to='newsletter.subscribersgroup')),
            ],
            options={
                'verbose_name': 'message de diffusion',
                'verbose_name_plural': 'messages de diffusion',
                'ordering': ['-created_at'],
            },
        ),
    ]
