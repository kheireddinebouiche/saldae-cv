from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


USER_TYPE={
    ('adm', 'Administrateur'),
    ('cli', 'Utilisateur'),

}

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_identification = models.CharField(max_length=100, null=True, blank = True)
    user_type = models.CharField(max_length=3, choices=USER_TYPE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.num_identification)
        super(Profile, self).save(*args, **kwargs)

NIV_COMP= {
    ('deb', 'Débutant'),
    ('int', 'Intermediaire'),
    ('ava', 'Avancer'),
    ('exp', 'Expert'),
}


class Competences(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100, null=True, blank=True)
    niveau = models.CharField(max_length=4, choices=NIV_COMP ,null=True, blank=True)

    class Meta:
        verbose_name="Compétence"
        verbose_name_plural="Compétences"

    def __str__(self):
        return self.titre

class Experience(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    nbr_annee = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name="Experience"
        verbose_name_plural="Experiences"

    def __str__(self):
        return self.user.username



INT_DIP ={
    ('dea', "Diplôme d'études approfondies"),
    ('bt', "Brevet de technicien"),
    ('bts', "Brevet de technicien supérieure"),
    ('cmp', "Certificat de maitrise professionnel"),
    ('doc', "Docteur d'état"),
    ('ing', 'Ingénieur'),
}

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    niveau = models.CharField(max_length=100, null=True, blank=True)
    diplome = models.CharField(max_length=3, choices=INT_DIP, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name="Education"
        verbose_name_plural="Educations"

    def __str__(self):
        return self.user.username





