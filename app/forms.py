from django import forms


class AddTovar(forms.Form):
    title = forms.CharField(max_length=25)
    sell = forms.IntegerField(min_value=0)
