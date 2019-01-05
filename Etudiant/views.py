# from django.shortcuts import HttpResponseRedirect
# from .forms import InscriptionForm, SujetForm
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.contrib.auth import logout
from django.views.generic import ListView
from .models import Sujet, Cours, Domaine


# # Create your views here.

# # View who display the formulary Inscription
# # def inscription(request):

# #     if request.method == "POST":
# #         form = InscriptionForm(request.POST or None)

# #         if form.is_valid():
# #             pseaudo = form.cleaned_data['pseaudo']
# #             email = form.cleaned_data['email']
# #             password = form.cleaned_data['password']

# #             user = User.objects.create_user(pseaudo, email,
# #                                             password, is_staff=True)
# #             return redirect("accueil")
# #     else:
# #         form = InscriptionForm()

# #     return render(request, 'Etudiant/inscription.html', locals())


# # View who display the connexion formulary
# # def connexion(request):
# #     erros = False
# #     if request.method == "POST":
# #         form = ConnexionForm(request.POST)
# #         if form.is_valid():
# #             pseaudo = form.cleaned_data['pseaudo']
# #             password = form.cleaned_data['password']
# #             # Nous verifions l'information fournis(s'il est inscrit)
# #             user = authenticate(username=pseaudo, password=password)
# #             if user:     # Si user est diff de none on le connect
# #                 login(request, user)
# #             else:       # Sinon on affiche un message d'erreur
# #                 erros = True
# #     else:
# #         form = ConnexionForm()

# #     return render(request, "Etudiant/connexion.html", locals())


# # views which deconnect user
# # def deconnexion(request):
# #     logout(request)
# #     return redirect(reverse('/Etudiant/connexion/'))


# Generic View who display the formulary to add a subjet
# class AjouterSujet(CreateView):
#     model = Sujet
#     template_name = "Etudiant/form_sujet.html"
#     # formulary to add a new subjet
#     # form_class = SujetForm
#     success_url = "/Etudiant/connexion"

# Redefine the form_valid function for add 'date' field before save
# define on html page
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.date = self.request.POST.get('date')
#         if self.request.user.is_authenticated:
#             self.object.user = self.request.user
#         self.object.save()

#         return HttpResponseRedirect(self.get_success_url())


# # View who display the list of Cours
class ListCours(ListView):
    model = Cours
    template_name = "Etudiant/cours_page.html"
    context_object_name = "cours"

    # Redefine queryset to precise the cours display
    def get_queryset(self):
        return Cours.objects.filter(domaine__id=self.kwargs['id'],
                                    domaine__slug=self.kwargs['slug']
                                    ).order_by('Nom')

    # Redefine context to display in another color the domaine selected
    def get_context_data(self, **kwargs):

        context = super(ListCours, self).get_context_data(**kwargs)

        context['domainechoisie'] = Domaine.objects.get(
                                            id=self.kwargs['id'],
                                            slug=self.kwargs['slug'])

        return context


# # View who display the list Subjet
class ListSujet(ListView):
    model = Sujet
    template_name = "Etudiant/sujets_page.html"
    context_object_name = "sujets"

    # Redefine queryset to precise the subjet display
    def get_queryset(self):
        return Sujet.objects.filter(cours__id=self.kwargs['id'],
                                    cours__slug=self.kwargs['slug']
                                    ).order_by('-date')

    # Redefine context to display the domaine and cours selected
    def get_context_data(self, **kwargs):

        context = super(ListSujet, self).get_context_data(**kwargs)

        # Add cours in context
        context['cours'] = Cours.objects.filter(
                                    domaine__Nom=self.kwargs['Nom'])

        # Add domainechoisie to point Domaine chose
        context['domainechoisie'] = Domaine.objects.get(Nom=self.kwargs['Nom'])

        # Add courchoisie to point Domaine chose
        context['courchoisie'] = Cours.objects.get(id=self.kwargs['id'],
                                                   slug=self.kwargs['slug'])

        return context
