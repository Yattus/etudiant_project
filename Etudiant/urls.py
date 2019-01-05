# # from django.contrib.signals import pre_delete
# # from .models import Sujet
# # from .forms import InscriptionForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import views as authViews
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
        # # url through home page
        url(r'^accueil/', TemplateView.as_view(
            template_name='Etudiant/accueil.html'),
            name='accueil'
            ),

        # url through domaine page who display the domaines names
        url(r'^domaines/', TemplateView.as_view(
            template_name='Etudiant/domaine_page.html'),
            name='domaines_page'
            ),

        # url through cours page who display the cours names
        url(r'^cours/(?P<id>\d+)-(?P<slug>.+)',
            views.ListCours.as_view(),
            name='cours_page'
            ),

        # url through sujets page who display the sujets names
        url(r'^sujets/(?P<id>\d+)-(?P<slug>.+)-(?P<Nom>.+)?$',
            views.ListSujet.as_view(),
            name='sujets_page'
            ),

        # url(r'^ajouter_encors_un_sujet_ou_retourne.html/',
        #     TemplateView.as_view(
        #         template_name='Etudiant/ajouter_sujet_or.html'),
        #     name='ajouter_encors_un_sujet_ou_non'
        #     ),

        # url(r'^ajouter_sujet/', login_required(views.AjouterSujet.as_view(),
        #     login_url='/Etudiant/connexion/'),
        #     name="ajouter_sujet"
        #     ),

        # url(r'^connexion/$', views.connexion, name='connexion'),
        # url(r'^connexion/$', authViews.login,
        #     {'template_name': 'Etudiant/connexion.html'},
        #     name='connexion'),

        # url(r'^deconnexion/$', authViews.logout,
        #     {'next_page': '/Etudiant/accueil'},
        #     name='deconnexion'),

        # url(r'^inscription/$', views.inscription, name="inscription"),
        # # url(r'^inscription/$', views.Inscription.as_view(),
        # name="inscription" ),

        # url(r'change_password/$', authViews.password_change,
        #     name='change_password'),
]
