from django.contrib import admin
from livres.models import Livre, Auteur, AuteurAdmin,Categorie, LivreAdmin, Etat

admin.site.register(Categorie)
admin.site.register(Etat)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Auteur, AuteurAdmin)
