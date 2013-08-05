from django import forms

class BookmarkForm(forms.Form):
    Title = forms.CharField(max_length=1024,required=False,widget=forms.TextInput(attrs={'size':'55'}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'size':'55'}),required=False)
    Url = forms.CharField(max_length=5024,required=False,widget=forms.TextInput(attrs={'size':'55'}))
    Tag =  forms.CharField(max_length=5024,required=False,widget=forms.TextInput(attrs={'size':'55'}))
    Private = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    Name = forms.CharField(max_length=1024,required=False,widget=forms.TextInput(attrs={'size':'55'}))
    Password = forms.CharField(widget=forms.PasswordInput(),required=False)
    Origin = forms.CharField(max_length=15,required=False,widget=forms.HiddenInput())
    Url = forms.CharField(max_length=5024,required=False,widget=forms.HiddenInput())

class SearchForm(forms.Form):
    Search = forms.CharField(max_length=1024,required=False,widget=forms.TextInput(attrs={'size':'55'}))
    Own = forms.BooleanField(required=False)
    
