from django import forms
from livres.models import Livre, Auteur, AuteurLivre


class EditLivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        exclude = []


class LivreSearchForm(forms.Form):
    titre = forms.CharField(max_length=100,
                            required=False)
    auteur = forms.CharField(max_length=100,
                             required=False)
