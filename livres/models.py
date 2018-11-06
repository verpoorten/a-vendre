from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL


class Personne(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    localite = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nom.upper() + ", " + self.prenom

    @staticmethod
    def find_all():
        return Personne.objects.all()

    @staticmethod
    def find_personne_by_user(user):
        try:
            return Personne.objects.get(user=user)
        except Exception:
            return None

    @staticmethod
    def find_by_id(an_id):
        return Personne.objects.get(pk=an_id)


class AuteurAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom']


class Auteur(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    prenom = models.CharField(max_length=100, blank=True, null=True)

    @staticmethod
    def find_all():
        return Auteur.objects.all().order_by('nom', 'prenom')

    @staticmethod
    def find_auteur(an_id):
        return Auteur.objects.get(pk=an_id)

    def __str__(self):
        return self.nom.upper() + ", " + self.prenom


class Categorie(models.Model):
    libelle = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.libelle


class LivreAdmin(admin.ModelAdmin):
    search_fields = ['titre', 'auteurs__nom', 'auteurs__prenom']
    raw_id_fields = ('auteurs', )
    list_display = ('titre', 'get_auteurs')
    list_filter = ('auteurs',)


class Livre(models.Model):
    LANGUE = (
        ('FR', 'Français'),
        ('ENG', 'Anglais')
    )
    FORMAT = (
        ('POCHE', 'Poche'),
        ('CARTONNE', 'Cartonné')
    )

    titre = models.CharField(max_length=100, blank=False, null=False)
    langue = models.CharField(max_length=5, choices=LANGUE, default='FR')
    categorie = models.ForeignKey(Categorie, blank=True, null=True, on_delete=CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modification = models.DateTimeField(auto_now=True, blank=True, null=True)
    remarque = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=15, choices=FORMAT, blank=True, null=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(
        upload_to='livre_images',
        null=True,
        blank=True,
        verbose_name="image"
    )
    vendu = models.BooleanField(default=False)
    auteurs = models.ManyToManyField(Auteur, related_name='livre_liste')

    def __str__(self):
        return self.titre

    @staticmethod
    def search(**kwargs):
        qs = Livre.objects

        if kwargs.get("titre"):
            print(kwargs['titre'])
            qs = qs.filter(titre__icontains=kwargs['titre'])
        if kwargs.get("auteur"):
            print(kwargs['auteur'])
            qs = qs.filter(auteurs__nom__icontains=kwargs['auteur'])

        return qs.select_related('categorie')

    def get_auteurs(self):
        return " - ".join(["{}, {}".format(p.nom, p.prenom) for p in self.auteurs.all()])
