from django import forms
from django.contrib import messages
from .models import Link


class AddLinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update(
            {'class': 'form-control', })

    class Meta:

        model = Link
        fields = ('url', )
        labels = {
            'url': 'Add Product',
        }
