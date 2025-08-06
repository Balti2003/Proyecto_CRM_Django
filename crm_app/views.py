from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, FormView, DetailView, UpdateView, ListView, DeleteView
from .forms import LoginForm, RegistrationForm, ContactForm, ClientCreateForm, CompanyCreateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Client, Company, Interaction

# Vistas generales
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


# Vistas de clientes
@method_decorator(login_required, name='dispatch')
class ClientListView(ListView):
    model = Client
    template_name = '../templates/clients/client_list.html'
    context_object_name = 'clients'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Client.objects.all().order_by('created_at')


@method_decorator(login_required, name='dispatch')
class ClientDetailView(DetailView):
    model = Client
    template_name = '../templates/clients/client_detail.html'
    context_object_name = 'client'
    
    def get_initial(self):
        self.initial['client_pk'] =  self.get_object().pk
        return super().get_initial()
    
    def get_success_url(self):
        return reverse('client_detail', args=[self.get_object().pk])


@method_decorator(login_required, name='dispatch')
class ClientCreateView(CreateView):
    template_name = '../templates/clients/client_create.html'
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy('client_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Cliente creado correctamente")
        return super(ClientCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ClientUpdateView(UpdateView):
    template_name = '../templates/clients/client_update.html'
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Cliente editado correctamente")
        return super(ClientUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('client_detail', args=[self.object.pk])


@method_decorator(login_required, name='dispatch')
class ClientDeleteView(DeleteView):
    model = Client
    template_name = '../templates/clients/client_delete.html'
    success_url = reverse_lazy('client_list')
    context_object_name = 'client'   

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Cliente eliminado correctamente")
        return super(ClientDeleteView, self).form_valid(form)


# Vistas de empresas
@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
    model = Company
    template_name = '../templates/companies/company_list.html'
    context_object_name = 'companys'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Company.objects.all().order_by('created_at')


@method_decorator(login_required, name='dispatch')
class CompanyDetailView(DetailView):
    model = Company
    template_name = '../templates/companies/company_detail.html'
    context_object_name = 'company'
    
    def get_initial(self):
        self.initial['company_pk'] =  self.get_object().pk
        return super().get_initial()
    
    def get_success_url(self):
        return reverse('company_detail', args=[self.get_object().pk])


@method_decorator(login_required, name='dispatch')
class CompanyCreateView(CreateView):
    template_name = '../templates/companies/company_create.html'
    model = Company
    form_class = CompanyCreateForm
    success_url = reverse_lazy('company_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Empresa creada correctamente")
        return super(CompanyCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    template_name = '../templates/companies/company_update.html'
    model = Company
    form_class = CompanyCreateForm
    success_url = reverse_lazy('company_list')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Empresa editada correctamente")
        return super(CompanyUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('company_detail', args=[self.object.pk])


@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = '../templates/companies/company_delete.html'
    success_url = reverse_lazy('company_list')
    context_object_name = 'company'   

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Empresa eliminada correctamente")
        return super(CompanyDeleteView, self).form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))