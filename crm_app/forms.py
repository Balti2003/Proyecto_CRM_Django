from django import forms
from django.contrib.auth.models import User
from .models import Client, Company, Interaction

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email",
            "password",
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
    
        return user
    
    
class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre'}),
        label="Nombre"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}),
        label="Correo electrónico"
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'id_mensaje', 'rows': 5}),
        label="Mensaje"
    )
    

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "assigned_to",
        ]
        

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "address",
            "website",
        ]
        

class InteractionCreateForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = [
            "client",
            "user",
            "date",
            "type",
            "notes",
        ]