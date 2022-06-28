from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('personnel_list', views.personnels_list, name='personnel-list'),
    path('conseils_list', views.conseils_list, name='conseils-list'),
    path('audience_list', views.audience_list, name='audience-list'),
    path('client_list', views.clients_list, name='client-list'),
    path('dossier_list', views.dossiers_list, name='dossier-list'),
    path('honoraire_list', views.honoraire_list, name='honoraire-list'),
    path('client_add', views.client_add, name='client-add'),
    path('personnel_add', views.personnel_add, name='personnel-add'),
    path('dossier_add', views.dossier_add, name='dossier-add'),
    path('conseil_add', views.conseil_add, name='conseil-add'),
    path('audience_add', views.audience_add, name='audience-add'),
    path('honoraire_add', views.honoraire_add, name='honoraire-add'),
    path('client_update/<str:pk>', views.client_update, name='client-update'),
    path('personnel_update/<str:pk>', views.personnel_update, name='personnel-update'),
    path('dossier_update/<str:pk>', views.dossier_update, name='dossier-update'),
    path('conseil_update/<str:pk>', views.conseil_update, name='conseil-update'),
    path('audience_update/<str:pk>', views.audience_update, name='audience-update'),
    path('honoraire_update/<str:pk>', views.honoraire_update, name='honoraire-update'),
    path('client_delete/<str:pk>', views.client_delete, name='client-delete'),
    path('personnel_delete/<str:pk>', views.personnel_delete, name='personnel-delete'),
    path('dossier_delete/<str:pk>', views.dossier_delete, name='dossier-delete'),
    path('conseil_delete/<str:pk>', views.conseil_delete, name='conseil-delete'),
    path('audience_delete/<str:pk>', views.audience_delete, name='audience-delete'),
    path('honoraire_delete/<str:pk>', views.honoraire_delete, name='honoraire-delete'),
    path('apropos', views.apropos, name='apropos-app')
]

