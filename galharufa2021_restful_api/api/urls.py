from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),

    # Admin URLs

    path('pessoas-admin/', views.getPessoasAdmin),
    path('atores-admin/', views.getAtoresAdmin),
    path('figuracoes-admin/', views.getFiguracoesAdmin),
    path('modelos-masculinos-admin/', views.getModelosMasculinosAdmin),
    path('modelos-femininos-admin/', views.getModelosFemininosAdmin),
    path('criancas-admin/', views.getCriancasAdmin),

    path('pessoa-admin/<slug:slug>/', views.getPessoaAdmin),
    path('ator-admin/<slug:slug>/', views.getAtorAdmin),
    path('figuracao-admin/<slug:slug>/', views.getFiguracaoAdmin),
    path('modelo-masculino-admin/<slug:slug>/', views.getModeloMasculinoAdmin),
    path('modelo-feminino-admin/<slug:slug>/', views.getModeloFemininoAdmin),
    path('crianca-admin/<slug:slug>/', views.getCriancaAdmin),

    # Non-admin URLs

    path('atores/', views.getAtores),
    path('figuracoes/', views.getFiguracoes),
    path('modelos-masculinos/', views.getModelosMasculinos),
    path('modelos-femininos/', views.getModelosFemininos),
    path('criancas/', views.getCriancas),

    path('ator/<slug:slug>/', views.getAtor),
    path('figuracao/<slug:slug>/', views.getFiguracao),
    path('modelo-masculino/<slug:slug>/', views.getModeloMasculino),
    path('modelo-feminino/<slug:slug>/', views.getModeloFeminino),
    path('crianca/<slug:slug>/', views.getCrianca),
]
