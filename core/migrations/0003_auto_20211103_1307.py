# Generated by Django 3.1 on 2021-11-03 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211103_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competences',
            options={'verbose_name': 'Compétence', 'verbose_name_plural': 'Compétences'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
        migrations.AddField(
            model_name='competences',
            name='niveau',
            field=models.CharField(blank=True, choices=[('exp', 'Expert'), ('ava', 'Avancer'), ('deb', 'Débutant'), ('int', 'Intermediaire')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='competences',
            name='titre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='diplome',
            field=models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='niveau',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='nbr_annee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('adm', 'Administrateur'), ('cli', 'Utilisateur')], max_length=3, null=True),
        ),
    ]
