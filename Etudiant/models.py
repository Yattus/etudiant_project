# from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os


# Une fonction pour renommer les photo de profil
# def renamePhoto(instance, fichier):
#     return "Photo_Profil/{}_{}_{}".format(instance.id,
#                                           instance.user.username, fichier)


def renameSujet(instance, fichier):
    return "Sujets/{0}/{1}/{2}_{3}".format(instance.domaine.Nom,
                                           instance.cours.Nom,
                                           instance.date, fichier)


# # TABALE DES UTILISATEUR
# class Profil(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#     photo = models.FileField(null=True, blank=True,
#                              upload_to=renamePhoto,
#                              verbose_name=_("Photo de profile"))

#     class Meta:
#         verbose_name = _('Membre')
#         verbose_name_plural = _('Membres')

#     def __str__(self):
#         return "hello! {}".format(self.user)


# TABLE for the sujets
class Sujet(models.Model):
    """Sujet"""
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Sujet name, example: TD, devoir, or Examen
    nom = models.CharField(max_length=100)

    # is domaine's name
    domaine = models.ForeignKey('Domaine', on_delete=models.CASCADE)

    # is cours's name
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE)

    # is file's name
    fichier = models.FileField(upload_to=renameSujet)

    # is year made
    date = models.DateField(auto_now_add=False,
                            verbose_name=("Quel année ?:"))

    # is day put in website
    date_d_ajout = models.DateTimeField(auto_now_add=True,
                                        verbose_name=("Date de soumision"))

    # enable/desable display option
    affichable = models.BooleanField(default=0,
                                     verbose_name=("Affichabilité"))
    # slug = models.SlugField(max_length=100, null=True)

    class Meta:
        """Meta"""
        verbose_name = ("Sujet")
        verbose_name_plural = ("Sujets")
        ordering = ["domaine"]

    def __str__(self):
        """__str__"""
        return ("Examen de {}".format(self.cours))


# # TABLE for the cours
class Cours(models.Model):
    """Cours"""
    Nom = models.CharField(max_length=50)
    domaine = models.ForeignKey("Domaine", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    class Meta:
        """Meta"""
        verbose_name = ("Cours")
        verbose_name_plural = ("Cours")
        ordering = ["domaine"]

    def __str__(self):
        """__str__"""
        return ("{} ({})".format(self.Nom, self.domaine, self.slug))


# # TABLE for the fields
class Domaine(models.Model):
    """Domaine"""
    Nom = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    class Meta:
        """Meta"""
        verbose_name = ("Domaine")
        verbose_name_plural = ("Domaines")
        ordering = ["Nom"]

    def __str__(self):
        """__str__"""
        return self.Nom


# # ===================== SIDE OF SIGNALS ====================

# signal de creation automatique d'un profil associer a chaque new inscription
# @receiver(pre_save, sender=User)
# def creation_Profil_user(sender, instance, **kwargs):
#     # Liste des utilisateurs ayant un profil
#     profil = [p.user for p in Profil.objects.all()]
#     if instance not in profil:
#         # Si l'instance sauvez na pas de profil on en crée une
#         Profil.objects.create(user=instance)


# Signal de suppression du fichier(sujet) associer lorsqu'on efface un sujet
# signal who remove file's sujet if we delete the sujet in base
@receiver(pre_delete, sender=Sujet)
def supression_sujet(sender, instance, **kwargs):
    path = os.getcwd()
    os.chdir(path[:-8] + '/Dossiers')
    os.remove(instance.fichier.name)
    os.chdir(path)


# signal de remplisage automatique des Slug associers au models Domaine
# signal who associate to the slug's domaine making
@receiver(pre_save, sender=Domaine)
def slugDomaine(sender, instance, **kwargs):
    nom = instance.Nom.split(' ')
    nom = '-'.join(nom)
    instance.slug = ('Science-de-l-ingénieur-'+nom)


# signal de remplisage automatique des Slug associers au models Cours
# signal who associate to the slug's cours making
@receiver(pre_save, sender=Cours)
def slugCours(sender, instance, **kwargs):
    nom = instance.Nom.split(' ')
    nom = '-'.join(nom)
    instance.slug = ('Science-de-l-ingénieur-'+nom)
