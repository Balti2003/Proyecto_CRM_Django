from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from crm_app.views import HomeView, LoginView, RegisterView, LegalView, ContactView, logout_view
from crm_app.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView
from crm_app.views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("client/list/", ClientListView.as_view(), name="client_list"),
    path("client/create/", ClientCreateView.as_view(), name="client_create"),
    path("client/<pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client/<pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("client/<pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("company/list/", CompanyListView.as_view(), name="company_list"),
    path("company/create/", CompanyCreateView.as_view(), name="company_create"),
    path("company/<pk>/", CompanyDetailView.as_view(), name="company_detail"),
    path("company/<pk>/update/", CompanyUpdateView.as_view(), name="company_update"),
    path("company/<pk>/delete/", CompanyDeleteView.as_view(), name="company_delete"),
    #path("interaction/list/", InteractionListView.as_view(), name="interaction_list"),
    #path("interaction/create/", InteractionCreateView.as_view(), name="interaction_create"),
    #path("interaction/<pk>/", InteractionDetailView.as_view(), name="interaction_detail"),
    #path("interaction/<pk>/update/", InteractionUpdateView.as_view(), name="interaction_update"),
    #path("interaction/<pk>/delete/", InteractionDeleteView.as_view(), name="interaction_delete"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
