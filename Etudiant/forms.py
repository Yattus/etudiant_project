# from django import forms
# from .models import Sujet, Cours
# # from django.contrib.auth.models import User


# # here your forms


# class InscriptionForm(forms.Form):
#     pseaudo = forms.CharField(max_length=100, label="Nom d'utilisateur")
#     email = forms.EmailField(label="Votre mail")
#     password = forms.CharField(label="Mot de passe",
#                                widget=forms.PasswordInput)

# #     class Meta:
# #         model = User
# #         fields = ('pseaudo', 'email', 'Password')


# class ConnexionForm(forms.Form):
#     pseaudo = forms.CharField(max_length=100)
#     password = forms.CharField(label="Mot de passe",
#                                widget=forms.PasswordInput)


# class SujetForm(forms.ModelForm):
#     # dat= forms.DateField()

#     class Meta:

#         model = Sujet
#         # fields = '__all__'
#         fields = ('fichier', 'cours', 'domaine')


# class CoursForm(forms.ModelForm):

#     class Meta:
#         model= Cours
#         fields= '__all__'
