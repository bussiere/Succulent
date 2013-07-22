from django import forms

class BookmarkForm(forms.Form):
    title = forms.CharField(max_length=1024)
    Description = forms.CharField(max_length=1024)
    Url = forms.CharField(max_length=5024)
    cc_myself = forms.BooleanField(required=False)