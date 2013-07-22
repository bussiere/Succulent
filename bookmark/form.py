from django import forms

class BookmarkForm(forms.Form):
    Title = forms.CharField(max_length=1024,required=False)
    Description = forms.CharField(widget=forms.Textarea,required=False)
    Url = forms.CharField(max_length=5024,required=False)
    Private = forms.BooleanField(required=False)