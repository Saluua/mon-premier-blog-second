from django import forms
from .models import Post,Commentaire

class PostForm (forms.ModelForm) :
    class Meta :
        model = Post
        fields = ('titre','texte',)

class CommentaireForm (forms.ModelForm) :
    class Meta :
        model = Commentaire
        fields = ('nom','email','corps')

