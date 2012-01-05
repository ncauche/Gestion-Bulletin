# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from gestionScolaire.bulletin.models import Etudiant,Matiere,Note,Commentaire

def index(request):
    liste_etudiant = Etudiant.objects.all().order_by('nom')
    return render_to_response('bulletin/index.html', {'liste_etudiant': liste_etudiant})

def etudiant(request):
    return render_to_response('bulletin/etudiant.html')

def etudiantValidation(request):
    if request.POST['nom'] and request.POST['prenom']:
        e = Etudiant(nom=request.POST['nom'], prenom=request.POST['prenom'])
        e.save()
    else:
        liste_etudiant = Etudiant.objects.all().order_by('nom')
        return render_to_response('bulletin/index.html', {
                'liste_etudiant': liste_etudiant,
                'error_message': "Erreur de saisie : champs vide(s).",
                })

    return HttpResponseRedirect(reverse('gestionScolaire.bulletin.views.index'))

def matiereListe(request):
    liste_matiere = Matiere.objects.all().order_by('intituleMatiere')
    return render_to_response('bulletin/matiereListe.html', {'liste_matiere': liste_matiere})

def matiere(request):
    return render_to_response('bulletin/matiere.html')

def matiereValidation(request):
    if request.POST['intitule']:
        m = Matiere(intituleMatiere=request.POST['intitule'])
        m.save()
    else:
        liste_matiere = Matiere.objects.all().order_by('intituleMatiere')
        return render_to_response('bulletin/matiereListe.html', {
                'liste_matiere': liste_matiere,
                'error_message': "Erreur de saisie : champs vide(s).",
                })

    return HttpResponseRedirect(reverse('gestionScolaire.bulletin.views.matiereListe'))

def detail(request, etudiant_id):
    e = get_object_or_404(Etudiant, pk=etudiant_id)
    listeNote = Note.objects.filter(etudiant=etudiant_id).select_related()
    c = 0
    moyenne = 0.0
    while c <listeNote.count():
        moyenne = moyenne + listeNote[c].note
        c = c + 1
    moyenne = moyenne / Matiere.objects.all().count()
    try:
        comGen = Commentaire.objects.get(etudiant=e)
    except (KeyError, Commentaire.DoesNotExist):
        commentaire = ""
    else:
        commentaire = comGen.commentaire
    return render_to_response('bulletin/detail.html',  {'etudiant': e, 'listeNote': listeNote, 'moyenne': moyenne, 'commentaire':commentaire})

def saisie(request, etudiant_id):
    e = get_object_or_404(Etudiant, pk=etudiant_id)
    listeMatiere = Matiere.objects.all().order_by('intituleMatiere')
    return render_to_response('bulletin/saisie.html', {'etudiant': e, 'listeMatiere': listeMatiere})

def validation(request, etudiant_id):
    e = get_object_or_404(Etudiant, pk=etudiant_id)
    listeMatiere = Matiere.objects.all()
    c = 0
    while c <listeMatiere.count():
	n = float(request.POST['note'+str(listeMatiere[c].id)])
        try:
            r = Note.objects.get(matiere=listeMatiere[c], etudiant=e)
        except (KeyError, Note.DoesNotExist):
            r = Note(etudiant=e, matiere=listeMatiere[c], note=n, commentaire=request.POST['commentaire'+str(listeMatiere[c].id)])
            r.save()
        else:
            r.note=n
            r.commentaire=request.POST['commentaire'+str(listeMatiere[c].id)]
            r.save()
	c = c + 1
    return HttpResponseRedirect(reverse('gestionScolaire.bulletin.views.detail',args=(e.id,)))

def commentaire(request, etudiant_id):
    e = get_object_or_404(Etudiant, pk=etudiant_id)
    try:
        comGen = Commentaire.objects.get(etudiant=e)
    except (KeyError, Commentaire.DoesNotExist):
        commentaire = ""
    else:
        commentaire = comGen.commentaire
    return render_to_response('bulletin/commentaire.html',  {'etudiant': e, 'commentaire':commentaire})

def validCommentaire(request, etudiant_id):
    e = get_object_or_404(Etudiant, pk=etudiant_id)
    try:
        c = Commentaire.objects.get(etudiant=e)
    except (KeyError, Note.DoesNotExist):
        c = Commentaire(etudiant=e, commentaire=request.POST['commentaire'])
        c.save()
    else:
        c.commentaire=request.POST['commentaire']
        c.save()
    return HttpResponseRedirect(reverse('gestionScolaire.bulletin.views.detail',args=(e.id,)))
