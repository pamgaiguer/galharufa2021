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
    path('pessoas-admin/', views.getPessoasAdmin),
    path('pessoa-admin/<slug:slug>/', views.getPessoaAdmin),
    #path('pessoa-admin/cadastrar/', views.postPessoa),
    #path('pessoas/', views.getPessoas),
    #path('pessoa/<slug:slug>/', views.getPessoa),
]