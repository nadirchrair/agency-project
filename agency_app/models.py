from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name_cat = models.CharField(max_length=50)
    descreption = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name_cat


class Offre(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_offre = models.CharField(max_length=50)
    descreption = models.TextField()
    dureé = models.CharField(max_length=50)
    price = models.IntegerField()
    complete = models.BooleanField()
    photo = models.FileField(upload_to='offre', max_length=100)

    def __str__(self):
        return self.name_offre


class Reservation(models.Model):
    Offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    nm_tlphn = models.CharField(max_length=50)
    place_reservé = models.IntegerField()

    def __str__(self):
        return self.nom