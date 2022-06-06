from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) #BD doit assurer l'intégrité = doit refléter les choses réelles , intégration : BD est centrale, l'acces : limiter les droits d'accès.
    titre = models.CharField(max_length = 200)
    texte = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date= timezone.now() #affecter une date au post.
        self.save() 
    def __str__(self):
        return self.titre