from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, FormView, DetailView, UpdateView, ListView
from .forms import LoginForm, RegistrationForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client, Company, Interaction

# Create your views here.

class HomeView(TemplateView):
    template_name = "../templates/general/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_clientes"] = Client.objects.count()
        context["total_usuarios"] = User.objects.count()
        context["total_empresas"] = Company.objects.count()
        context["total_interacciones"] = Interaction.objects.count()
        
        return context
    
    
class LoginView(FormView):
    template_name = "../templates/general/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        usuario = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=usuario, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, "Has iniciado sesion correctamente")
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(self.request, messages.ERROR, "Usuario o contraseña incorrectos")
            return super(LoginView, self).form_valid(form)
        
class RegisterView(CreateView):
    model = User
    template_name = "../templates/general/register.html"
    success_url = reverse_lazy("login")
    form_class = RegistrationForm
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente")
        return super(RegisterView, self).form_valid(form)


class LegalView(TemplateView):
    template_name = '../templates/general/legal.html'
    
    
class ContactView(TemplateView, FormView):
    template_name = '../templates/general/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']
        
        messages.add_message(self.request, messages.SUCCESS, "Mensaje enviado correctamente")
        return super().form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))