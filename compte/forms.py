from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User


class ModifierNomUtilisateurForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)

class ModifierEmailForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

class ModifierMotDePasseForm(PasswordChangeForm):
    pass  # Utilisez le formulaire PasswordChangeForm par défaut

class AjouterUtilisateurForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
