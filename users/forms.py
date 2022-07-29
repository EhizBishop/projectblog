from django import forms
from . models import User


class UserRegister(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label=('Confirm Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['full_name','email','username','password1','password2','address','profile_pix']
        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'profile_pix':forms.FileInput(attrs={'class':'form-control'}),
        }
        