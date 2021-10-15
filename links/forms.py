from django import forms
from django.contrib import messages
from .models import Link


class AddLinkForm(forms.ModelForm):

    # def save(self, commit=True):

    #     product = super(AddLinkForm, self).save(commit=False)
    #     product_name = self.cleaned_data['article_name']
    #     if Link.objects.filter(article_name=self.cleaned_data['article_name']).exists():
    #         messages.success('Sorry Article already in Database.')
    #     if commit:
    #         product.save()

    class Meta:

        model = Link
        fields = ('url', )
