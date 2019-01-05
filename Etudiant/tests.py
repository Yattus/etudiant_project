from django.test import TestCase
from .models import Domaine, Cours, Sujet
from datetime import datetime
from django.core.files import File

# Create your tests here.


# Test table domaine
class TestDomaineTable(TestCase):

    @classmethod
    def setUpTestData(cls):
        Domaine.objects.create(Nom='Génie Informatique')

    def test_verifications(self):
        # test field slug if is made
        self.assertTrue(Domaine.objects.filter(
            slug="Science-de-l-ingénieur-Génie-Informatique").exists())


# Test table cours
class TestCoursTable(TestCase):

    @classmethod
    def setUpTestData(cls):
        Domaine.objects.create(Nom='Génie Electrique')
        Cours.objects.create(Nom='Algorithme', domaine=Domaine.objects.get(
            Nom="Génie Electrique"))

    def test_verifications(self):
        # test field slug if is made and table in same time
        self.assertTrue(Domaine.objects.filter(
            slug="Science-de-l-ingénieur-Génie-Electrique").exists())
        self.assertTrue(Cours.objects.filter(
            slug="Science-de-l-ingénieur-Algorithme").exists())


class TestSujetsTable(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Domaine.objects.create(Nom='Génie Eléctromécanique')
        # Cours.objects.create(Nom='Résistances des matériaux')
        Sujet.objects.create(
            cour=Cours.objects.get(Nom='Résistances des matériaux'),
            domaine=Domaine.objects.get(Nom='Génie Eléctromécanique'),
            date=datetime.date(1997, 3, 24),
            fichier=File(open('/home/alex/Downloads/4-Enonces.pdf'))
        )

        def test_verifications(self):
            # sujets if exist
            self.assertTrue(Sujet.objects.filter(
                domaine__Nom__contains='Génie Eléctromécanique').exists())
