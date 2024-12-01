from django import forms
from .models import Multimedia

class MultimediaForm(forms.ModelForm):
    class Meta:
        model = Multimedia
        fields = ['title', 'description', 'media_file', 'media_type']
