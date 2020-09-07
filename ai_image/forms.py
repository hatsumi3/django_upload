from django import forms
from django.core.exceptions import ValidationError

from .models import Document

class DocumentForm(forms.ModelForm):
    """Document classのモデルフォーム

    Args:
        forms ([type]): Document classのモデルフォーム
    """

    def __init__(self, *args, **kwargs):

        super(DocumentForm, self).__init__(*args, **kwargs)
        # bootstrap用にclassに’form-control’を追記
        # for field in self.fields.values():
        #     field.widget.attrs["class"] = "form-control"
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['photo'].widget.attrs['class'] = 'form-control'


    def clean_description(self):
        data = self.cleaned_data['description']
        # if "test" not in data:
        #     raise ValidationError("description error")
        return data

    class Meta:
        model = Document
        fields = ('description', 'photo')
