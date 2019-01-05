from django.contrib import admin
# from django.utils.text import Truncator
from .models import Cours, Sujet, Domaine
# # Register your models here.


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('Nom', 'apercu_email')
#     list_filter = ('Nom',)
#     ordering = ('date',)
#     date_hierarchy = 'date'
#     search_fields = ('date', 'Nom')

#     def apercu_email(self, user):
#         """ retourne les 20 premier char de l'Email"""

#         return Truncator(user.email).chars(20, truncate='...')

#     apercu_email.short_description = 'Email'


admin.site.register(Cours)
admin.site.register(Sujet)
admin.site.register(Domaine)
