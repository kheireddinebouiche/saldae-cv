# Generated by Django 3.1 on 2021-11-03 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211103_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
        migrations.AddField(
            model_name='education',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='competences',
            name='niveau',
            field=models.CharField(blank=True, choices=[('ava', 'Avancer'), ('deb', 'Débutant'), ('int', 'Intermediaire'), ('exp', 'Expert')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='diplome',
            field=models.CharField(blank=True, choices=[('doc', "Docteur d'état"), ('cmp', 'Certificat de maitrise professionnel'), ('bt', 'Brevet de technicien'), ('ing', 'Ingénieur'), ('bts', 'Brevet de technicien supérieure'), ('dea', "Diplôme d'études approfondies")], max_length=3, null=True),
        ),
    ]
