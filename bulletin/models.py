from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __unicode__(self):
	return self.nom

class Matiere(models.Model):
    intituleMatiere = models.CharField(max_length=100)

    def __unicode__(self):
	return self.intituleMatiere

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant)
    matiere = models.ForeignKey(Matiere)
    note = models.FloatField()
    commentaire = models.CharField(max_length=200)

    def __unicode__(self):
	return u'n%s' % self.note

class Commentaire(models.Model):
    etudiant = models.ForeignKey(Etudiant)
    commentaire = models.CharField(max_length=200)

    def __unicode__(self):
	return u'm%f' % self.commentaire
