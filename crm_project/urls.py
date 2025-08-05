from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from crm_app.views import HomeView, LoginView, RegisterView, LegalView, ContactView, logout_view

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    #path("clients/list/", ClientsListView.as_view(), name="client_list"),
    #path("clients/<pk>/", ClientsDetailView.as_view(), name="client_detail"),
    #path("clients/create/", ClientsCreateView.as_view(), name="client_create"),
    #path("clients/update/<pk>/", ClientUpdateView.as_view(), name="client_update"),
    #path("clients/delete/<pk>/", ClientDeleteView.as_view(), name="client_delete"),
    #path("interactions/list/", InteractionsListView.as_view(), name="interaction_list"),
    #path("interactions/<pk>/", InteractionsDetailView.as_view(), name="interaction_detail"),
    #path("interactions/create/", InteractionCreateView.as_view(), name="interaction_create"),
    #path("interactions/update/<pk>/", InteractionUpdateView.as_view(), name="interaction_update"),
    #path("interactions/delete/<pk>/", InteractionDeleteView.as_view(), name="interaction_delete"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
