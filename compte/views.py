from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ModifierNomUtilisateurForm, ModifierEmailForm, ModifierMotDePasseForm, AjouterUtilisateurForm

@login_required
def modifier_compte(request):
    user = request.user

    modifier_nom_utilisateur_form = ModifierNomUtilisateurForm(instance=user)
    modifier_email_form = ModifierEmailForm(instance=user)
    modifier_mot_de_passe_form = ModifierMotDePasseForm(request.user)
    ajout_utilisateur_form = AjouterUtilisateurForm()

    if request.method == 'POST':
        if 'modifier-username' in request.POST:
            modifier_nom_utilisateur_form = ModifierNomUtilisateurForm(request.POST, instance=user)
            if modifier_nom_utilisateur_form.is_valid():
                modifier_nom_utilisateur_form.save()
                messages.success(request, 'Nom d\'utilisateur modifié avec succès.')
                return redirect('compte:modifier_compte')
        elif 'modifier-email' in request.POST:
            modifier_email_form = ModifierEmailForm(request.POST, instance=user)
            if modifier_email_form.is_valid():
                modifier_email_form.save()
                messages.success(request, 'Adresse e-mail modifiée avec succès.')
                return redirect('compte:modifier_compte')
        elif 'modifier-password' in request.POST:
            modifier_mot_de_passe_form = ModifierMotDePasseForm(request.user, request.POST)
            if modifier_mot_de_passe_form.is_valid():
                modifier_mot_de_passe_form.save()
                messages.success(request, 'Mot de passe modifié avec succès.')
                return redirect('compte:modifier_compte')
        elif 'ajouter-utilisateur' in request.POST:
            ajout_utilisateur_form = AjouterUtilisateurForm(request.POST)
            if ajout_utilisateur_form.is_valid():
                ajout_utilisateur_form.save()
                messages.success(request, 'Nouvel utilisateur ajouté avec succès.')
                return redirect('compte:modifier_compte')

    return render(request, 'compte/modifier_compte.html', {
        'modifier_nom_utilisateur_form': modifier_nom_utilisateur_form,
        'modifier_email_form': modifier_email_form,
        'modifier_mot_de_passe_form': modifier_mot_de_passe_form,
        'ajout_utilisateur_form': ajout_utilisateur_form,
    })


def compte(request):
    conn_form = AuthenticationForm(data=request.POST or None)

    if request.method == 'POST':
        if 'connexion' in request.POST:
            if conn_form.is_valid():
                user = conn_form.get_user()
                login(request, user)
                return redirect('ppm:dashboard')

    context = {
        'conn_form': conn_form,
    }
    return render(request, 'compte/compte.html', context)
