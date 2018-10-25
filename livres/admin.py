from django.contrib import admin
from livres.models import Livre, Auteur, AuteurAdmin, AuteurLivre, AuteurLivreAdmin,Categorie

admin.site.register(Categorie)

admin.site.register(Livre)
admin.site.register(Auteur, AuteurAdmin)
admin.site.register(AuteurLivre, AuteurLivreAdmin)
