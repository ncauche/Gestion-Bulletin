from django.conf.urls.defaults import *

urlpatterns = patterns('gestionScolaire.bulletin.views',
    (r'^$', 'index'),
    (r'^etudiant/$', 'etudiant'),
    (r'^etudiantValidation/$', 'etudiantValidation'),
    (r'^matiereListe/$', 'matiereListe'),
    (r'^matiere/$', 'matiere'),
    (r'^matiereValidation/$', 'matiereValidation'),
    (r'^(?P<etudiant_id>\d+)/$', 'detail'),
    (r'^(?P<etudiant_id>\d+)/saisie/$', 'saisie'),
    (r'^(?P<etudiant_id>\d+)/validation/$', 'validation'),
    (r'^(?P<etudiant_id>\d+)/commentaire/$', 'commentaire'),
    (r'^(?P<etudiant_id>\d+)/validCommentaire/$', 'validCommentaire'),
)
