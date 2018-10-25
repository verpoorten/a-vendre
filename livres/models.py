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
    search_fields = ['nom']


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
    search_fields = ['titre']


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

    @staticmethod
    def find_all():
        return Livre.objects.all().order_by('titre')

    @staticmethod
    def find_livre(an_id):
        return Livre.objects.get(pk=an_id)


    def __str__(self):
        return self.titre

    @staticmethod
    def find_by_etat_lecture(etat_lecture, user):
        person = Personne.find_personne_by_user(user)
        livres = []
        if etat_lecture:
            lecture_liste = Lecture.objects.filter(personne=person)
            for lecture in lecture_liste:
                livres.append(lecture.livre)
            return livres
        else:
            liste_livre = Livre.objects.all()
            for livre in liste_livre:
                if not Lecture.objects.filter(personne=person):
                    livres.append(livre)
            return livres





    @staticmethod
    def find_by_titre(titre):
        return Livre.objects.filter(titre__icontains=titre)



    @staticmethod
    def search(**kwargs):
        print('search')
        qs = Livre.objects


        if kwargs.get("titre"):
            print(kwargs['titre'])
            qs = qs.filter(titre__icontains=kwargs['titre'])
        if kwargs.get("auteur"):
            print(kwargs['auteur'])
            qs = qs.filter(auteurs__nom__icontains=kwargs['auteur'])
        return qs.select_related('categorie')