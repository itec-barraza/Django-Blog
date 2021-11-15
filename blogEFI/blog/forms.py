from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=40 , required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo'}))
    content = forms.CharField(label='Contenido' ,min_length=30, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Contenido'}))
    author = forms.CharField(label='Message',min_length=30 ,required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escriba aqui su mensaje', 'rows':'4'}))

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'author',
            'image',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Contenido'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'aria-describedby': 'id_image'})
        }