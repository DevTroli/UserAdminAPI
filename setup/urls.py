from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

# Importações necessárias para o Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Criamos um roteador padrão que gerenciará as rotas para os ViewSets
router = routers.DefaultRouter()

# Registra as rotas para o conjunto de visualizações de usuários
router.register(r"users", views.UserViewSet)

# Registra as rotas para o conjunto de visualizações de grupos
router.register(r"groups", views.GroupViewSet)

# Configura o schema do Swagger para gerar a documentação da API automaticamente
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",  # Título da documentação
        default_version="v1",  # Versão da API
        description="Documentação automática gerada pelo Swagger",  # Descrição da API
        terms_of_service="https://www.google.com/policies/terms/",  # Termos de serviço
        contact=openapi.Contact(
            email="pablotroli@outlook.com"
        ),  # Informações de contato
        license=openapi.License(name="Licença BSD"),  # Licença da API
    ),
    public=True,  # Define se a documentação será pública
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Inclui as rotas geradas automaticamente pelo roteador (para users/ e groups/)
    path("", include(router.urls)),
    # Rota para as URLs de autenticação padrão do DRF (login, logout)
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Rota para a interface do Swagger, onde será gerada a documentação interativa
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # Rota para a interface do Redoc, outra forma de visualizar a documentação da API
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
