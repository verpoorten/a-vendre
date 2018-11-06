from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from livres.models import Livre, Auteur, nouveautes_livres
from livres.forms import EditLivreForm, LivreSearchForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect


class LivresList(ListView):
    model = Livre

    ordering = ['titre']


class AuteursList(ListView):
    model = Auteur


class LivreDetail(DetailView):
    model = Livre

    def get_context_data(self, **kwargs):
        context = super(LivreDetail, self).get_context_data(**kwargs)

        cookie_key = "livre_{}".format(self.object.id)
        is_favori = False
        id_favori = self.request.COOKIES.get(cookie_key)
        if id_favori:
            is_favori = True

        context['is_favori'] = is_favori

        return context


class EditLivre(LoginRequiredMixin, UpdateView):
    model = Livre
    form_class = EditLivreForm

    def get_success_url(self):
        return reverse('livre_detail', args=(self.object.pk,))


def home(request):
    return render(
        request,
        'base.html',
        {'nouveautes': nouveautes_livres}
    )


def livre_search(request):
    form = LivreSearchForm(request.POST or None)
    livres = None
    if form.is_valid() and form.cleaned_data:
        titre = form.cleaned_data.get('titre')
        auteur = form.cleaned_data.get('auteur')
        livres = Livre.search(titre=titre, auteur_nom=auteur).distinct()

    return render(
        request,
        'livres/livre_search.html',
        {
            'object_list': livres,
            'form': form,
        })


def favoris(request):
    ids = []
    for k, v in request.COOKIES.items():
        pos = k.find("livre_")
        if pos >= 0:
            ids.append(v)

    return render(
        request,
        'favoris.html',
        {
            'object_list': Livre.objects.filter(id__in=ids),
        })


def recherche_par_auteur(request, auteur_id):
    auteur = get_object_or_404(Auteur, pk=auteur_id)
    form = LivreSearchForm({'auteur': auteur})
    livres = []
    # if form.is_valid() and form.cleaned_data:
    livres = Livre.search(auteur=auteur).distinct()
    print(livres)
    return render(
        request,
        'livres/livre_search.html',
        {
            'object_list': livres,
            'form': form,
        })
    # return HttpResponseRedirect(reverse('livre_search'))