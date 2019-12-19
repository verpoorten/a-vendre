from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from livres.forms import EditLivreForm, LivreSearchForm
from livres.models import Livre, Auteur, nouveautes_livres
from livres.business.xls_utils import adjust_column_width


class LivresToExcel:

    def get_queryset(self):
        return Livre.objects.all().order_by('auteurs')

    def _to_workbook(self):
        return generate_workbook(self.get_queryset())

    def to_excel(self):
        return save_virtual_workbook(self._to_workbook())


def generate_workbook(livres):
    worksheet_title = "livres"
    workbook = Workbook()
    return _get_workbook(_build_lines(livres), workbook, worksheet_title)


def _build_lines(livres):
    content = []

    for livre in livres:
        content.append(
            [str(livre.get_auteurs()),
             str(livre.titre),
             str(livre.prix) if livre.prix else str('-'),
             str(livre.format) if livre.format else str('-')]
        )

    return content


def _get_workbook(content, workbook, worksheet_title):
    headers_title = ['Auteur', 'Titre', 'Prix', 'Format']

    worksheet1 = workbook.active
    worksheet1.title = worksheet_title
    worksheet1.append(headers_title)

    for line in content:
        worksheet1.append(line)
    adjust_column_width(worksheet1)
    return workbook


