# Generated by Django 3.1 on 2021-11-03 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211103_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='competences',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='competences',
            name='niveau',
            field=models.CharField(blank=True, choices=[('exp', 'Expert'), ('deb', 'Débutant'), ('ava', 'Avancer'), ('int', 'Intermediaire')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='diplome',
            field=models.CharField(blank=True, choices=[('bt', 'Brevet de technicien'), ('cmp', 'Certificat de maitrise professionnel'), ('ing', 'Ingénieur'), ('dea', "Diplôme d'études approfondies"), ('doc', "Docteur d'état"), ('bts', 'Brevet de technicien supérieure')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('cli', 'Utilisateur'), ('adm', 'Administrateur')], max_length=3, null=True),
        ),
    ]