from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True) #Nombre empresa
    address = models.TextField(blank=True, null=True) #Dirección de empresa
    website = models.URLField(blank=True, null=True) #Sitio web de empresa
    created_at = models.DateTimeField(auto_now_add=True) #Fecha de creación
    updated_at = models.DateTimeField(auto_now=True) #Fecha de ultima actualización
    
    def __str__(self):
        return self.name #Como se mostrara en el admin y otros lugares
    
class Client(models.Model):
    name = models.CharField(max_length=255) #Nombre del cliente
    email = models.EmailField(unique=True) #Email del cliente
    phone = models.CharField(max_length=50, blank=True) #Telefono del cliente
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, blank=True, null=True, 
        related_name='clients') #Empresa del cliente
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, 
        related_name='clients') #Asignado a tal usuario
    created_at = models.DateTimeField(auto_now_add=True) #Fecha de creación
    updated_at = models.DateTimeField(auto_now=True) #Fecha de ultima actualización
    
    def __str__(self):
        return self.name
    
class Interaction(models.Model):
    TYPE_CHOICES = [
        ('call', 'Llamada'),
        ('meeting', 'Reunión'),
        ('email', 'Email'),
        ('other', 'Otro'),    
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interactions') #Cliente relacionado
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='interactions') #Usuario que hizo la interaccion
    date = models.DateTimeField() #Fecha de la interaccion
    type = models.CharField(max_length=20, choices=TYPE_CHOICES) #Tipo de interaccion
    notes = models.TextField(blank=True) #Notas de la interaccion
    created_at = models.DateTimeField(auto_now_add=True) #Fecha de creación
    updated_at = models.DateTimeField(auto_now=True) #Fecha de ultima actualización
    
    def __str__(self):
        return f"{self.get_type_display()} con {self.client.name} el {self.date.strftime('%Y-%m-%d')}"
    