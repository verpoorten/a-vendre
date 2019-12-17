from django import forms
from livres.models import Livre, Auteur


class EditLivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        exclude = []


class LivreSearchForm(forms.Form):
    titre = forms.CharField(max_length=100,
                            required=False,
                            help_text="(Attention aux accents si vous cherchez 'étrange' et que c'est 'Etrange' qui est encodé ce ne sera pas trouvé!)")
    auteur = forms.CharField(max_length=100,
                             required=False)
