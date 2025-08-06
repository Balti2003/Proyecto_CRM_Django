from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from crm_app.views import HomeView, LoginView, RegisterView, LegalView, ContactView, logout_view, ClientListView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("client/list/", ClientListView.as_view(), name="client_list"),
    #path("client/<pk>/", ClientDetailView.as_view(), name="client_detail"),
    #path("client/create/", ClientCreateView.as_view(), name="client_create"),
    #path("client/update/<pk>/", ClientUpdateView.as_view(), name="client_update"),
    #path("client/delete/<pk>/", ClientDeleteView.as_view(), name="client_delete"),
    #path("interaction/list/", InteractionListView.as_view(), name="interaction_list"),
    #path("interaction/<pk>/", InteractionDetailView.as_view(), name="interaction_detail"),
    #path("interaction/create/", InteractionCreateView.as_view(), name="interaction_create"),
    #path("interaction/update/<pk>/", InteractionUpdateView.as_view(), name="interaction_update"),
    #path("interaction/delete/<pk>/", InteractionDeleteView.as_view(), name="interaction_delete"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
