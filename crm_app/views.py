from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, FormView, DetailView, UpdateView, ListView, DeleteView
from .forms import LoginForm, RegistrationForm, ContactForm, ClientCreateForm, CompanyCreateForm, InteractionCreateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Client, Company, Interaction
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

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


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = '../templates/general/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Contadores
        context['total_clients'] = Client.objects.count()
        context['total_companies'] = Company.objects.count()
        context['total_interactions'] = Interaction.objects.count()

        # Gráfico de pastel: Interacciones por tipo
        interactions_by_type = (
            Interaction.objects
            .values('type')
            .annotate(total=Count('id'))
        )
        context['interactions_labels'] = [item['type'] for item in interactions_by_type]
        context['interactions_data'] = [item['total'] for item in interactions_by_type]

        # Gráfico de barras: Clientes por empresa
        clients_per_company = (
            Company.objects
            .annotate(client_count=Count('clients'))
        )
        context['companies_labels'] = [company.name for company in clients_per_company]
        context['companies_data'] = [company.client_count for company in clients_per_company]

        return context


# Vistas de clientes
@method_decorator(login_required, name='dispatch')
class ClientListView(ListView):
    model = Client
    template_name = '../templates/clients/client_list.html'
    context_object_name = 'clients'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(company__name__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


@method_decorator(login_required, name='dispatch')
class ClientDetailView(DetailView):
    model = Client
    template_name = '../templates/clients/client_detail.html'
    context_object_name = 'client'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        context['interactions'] = client.interactions.all()
        return context


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
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(website__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


@method_decorator(login_required, name='dispatch')
class CompanyDetailView(DetailView):
    model = Company
    template_name = '../templates/companies/company_detail.html'
    context_object_name = 'company'



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


# Vistas de interacciones
@method_decorator(login_required, name='dispatch')
class InteractionDetailView(DetailView):
    model = Interaction
    template_name = '../templates/interactions/interaction_detail.html'
    context_object_name = 'interaction'


@method_decorator(login_required, name='dispatch')
class InteractionCreateView(CreateView):
    template_name = '../templates/interactions/interaction_create.html'
    model = Interaction
    form_class = InteractionCreateForm
    success_url = reverse_lazy('client_detail')

    def dispatch(self, request, *args, **kwargs):
        self.client = get_object_or_404(Client, pk=kwargs['client_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.client = self.client
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Interacción creada correctamente")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.client
        return context

    def get_success_url(self):
        return reverse('client_detail', args=[self.client.pk])


@method_decorator(login_required, name='dispatch')
class InteractionUpdateView(UpdateView):
    template_name = '../templates/interactions/interaction_update.html'
    model = Interaction
    form_class = InteractionCreateForm
    success_url = reverse_lazy('client_detail')

    def dispatch(self, request, *args, **kwargs):
        self.interaction = self.get_object()
        self.client = self.interaction.client
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.client = self.client
        messages.success(self.request, "Interacción actualizada correctamente")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client_detail', args=[self.client.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.client
        return context


@method_decorator(login_required, name='dispatch')
class InteractionDeleteView(DeleteView):
    model = Interaction
    template_name = '../templates/interactions/interaction_delete.html'
    success_url = reverse_lazy('client_detail')
    context_object_name = 'interaction'   

    def dispatch(self, request, *args, **kwargs):
        self.interaction = self.get_object()
        self.client = self.interaction.client
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Interacción eliminada correctamente")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('client_detail', args=[self.client.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.client
        return context
    

# Vista de logout   
@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))