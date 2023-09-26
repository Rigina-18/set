from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from ckeditor_uploader.fields import RichTextUploadingField
from django import forms

from .models import *


class PostCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='Category',
        widget=forms.Select(attrs={'class': 'form-select'}),
        queryset=Category.objects.all()
    )
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Text', widget=CKEditorUploadingWidget(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        exclude = ('author',)


class CommentCreateForm(forms.ModelForm):
    text = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('text',)
