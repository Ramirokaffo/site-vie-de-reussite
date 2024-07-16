# Generated by Django 4.2.9 on 2024-07-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0021_physicformationcmd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicformationcmd',
            name='formation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formation.formation', verbose_name='formation achetée'),
        ),
        migrations.AlterField(
            model_name='saleformation',
            name='formation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formation.formation', verbose_name='formation achetée'),
        ),
    ]
