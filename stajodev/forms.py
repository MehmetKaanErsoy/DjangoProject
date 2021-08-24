from django import forms
from .models import fakulteeekle, bolumekle, sorumlu_ekle
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from .filters import Fakulte


class FakulteEklee(forms.ModelForm):
    fakulte_ismii = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "type": "text",
        "Placeholder": "Fakülte Eklemek İçin Giriniz.",
    }))

    class Meta:
        model = fakulteeekle
        fields = ['fakulte_ismii', ]


class BolumEkle(forms.ModelForm):
    Bolum_ismi = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "type": "text",
        "Placeholder": "Bolum Eklemek İçin Giriniz.",
    }))
    fakulte_ismi = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px',
        'list': "fakulte_isimleriii",
        "type": "text",
        "Placeholder": "Fakülte seçiniz.",
    }))

    class Meta:
        model = bolumekle
        fields = ['Bolum_ismi', 'fakulte_ismi', ]


class SorumluEkle(forms.ModelForm):
    ünvanı = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "list": 'ünvan',
        "type": "text",
        "Placeholder": "Ünvan Seçiniz.",
    }))
    adisoyadi = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "type": "text",
        "Placeholder": "Adınız ve Soyadınız.",
    }))
    telefon = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "type": "text",
        "Placeholder": "Telefon Numaranız.",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "type": "text",
        "Placeholder": "Email Adresiniz.",
    }))
    fakulte = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "type": "text",
        "list": "fakulte_isimleriii",
        "Placeholder": "Fakülte Seçiniz.",
    }))
    bolum = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;',
        "list": 'bolumler',
        "type": "text",
        "Placeholder": "Bölüm Seçiniz.",
    }))

    class Meta:
        model = sorumlu_ekle
        fields = ['ünvanı', 'adisoyadi', 'telefon', 'email', 'fakulte', 'bolum']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label="Username", required=True, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'name': 'username',
                                   'placeholder': 'Kullanıcı adınız...',
                                   'style': 'margin-left:-190px;width:200px;height:30px;border-radius:5px;'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'name': 'password',
                                   'placeholder': 'Parolanız...',
                                   'style': 'margin-left:-190px;width:200px;height:30px;border-radius:5px;'}))


class passreset(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    bolum = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        'style': 'margin-left:10px; width:250px;height:40px;margin-top:30px',
        "type": "text",
        "Placeholder": "Email Adresiniz.",
    }))


class setPasswordform(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        'style': 'margin-left:10px; width:250px;height:40px;margin-top:30px',
        "type": "password",
        "Placeholder": "Yeni parolanız.",
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        'style': 'margin-left:10px; width:250px;height:50px;margin-top:30px',
        "type": "password",
        "Placeholder": "Yeni Parolanızı Tekrar Giriniz.",
    }))
