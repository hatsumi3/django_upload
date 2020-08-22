from django import forms
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

    class Meta:
        model = Document
        fields = ('description', 'photo')
