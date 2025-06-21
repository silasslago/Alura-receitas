from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='search', max_length=100, required=False)
    category_id = forms.IntegerField(label='category', required=False)