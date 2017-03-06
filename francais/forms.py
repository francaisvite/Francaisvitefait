from django import forms


class SubmitDocForm(forms.Form):
   
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    Stud_status = forms.CharField()
    uploadDoc = forms.FileField()  
    comment = forms.CharField(widget = forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)