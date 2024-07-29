# Generated by Django 4.2.9 on 2024-07-21 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='contenu')),
                ('is_visible', models.BooleanField(default=False, verbose_name='publié ?')),
                ('last_updated', models.DateTimeField(auto_now_add=True, verbose_name='modifié le')),
                ('created_at', models.DateField(auto_now=True, null=True, verbose_name='créé le')),
                ('rate', models.IntegerField(choices=[(0, 'Très mécontent'), (1, 'Mécontent'), (2, 'Indifférent'), (3, 'Satisfait'), (4, 'Très Satisfait')], default=4, verbose_name='note')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='auteur')),
            ],
            options={
                'verbose_name': 'témoignage',
                'verbose_name_plural': 'témoignages',
                'ordering': ['-created_at'],
            },
        ),
    ]
