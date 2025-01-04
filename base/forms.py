from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import TextDocument


class TextDocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False

    class Meta:
        model = TextDocument
        fields = ('title', 'text')
        widgets = {
            'text':CKEditor5Widget(
                attrs={'class':'django_ckeditor_5'},
                config_name='extends'
            )
        }