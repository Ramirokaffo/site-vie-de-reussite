# Generated by Django 4.2.9 on 2024-07-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_alter_subscribers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='add_unsubscribe_link',
            field=models.BooleanField(default=True, verbose_name='Ajouter le lien de désinscription'),
        ),
    ]
