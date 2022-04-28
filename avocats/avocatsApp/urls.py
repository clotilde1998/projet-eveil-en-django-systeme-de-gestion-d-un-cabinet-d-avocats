from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('personnel_list', views.personnels_list, name='personnel-list'),
    path('conseils_list', views.conseils_list, name='conseils-list'),
    path('redactions_list', views.redactions_list, name='redactions-list'),
    path('client_list', views.clients_list, name='client-list'),
    path('dossier_list', views.dossiers_list, name='dossier-list'),
    path('client_add', views.client_add, name='client-add'),
    path('personnel_add', views.personnel_add, name='personnel-add'),
    path('dossier_add', views.dossier_add, name='dossier-add'),
    path('conseil_add', views.conseil_add, name='conseil-add'),
    path('redactions_add', views.redactions_add, name='redactions-add'),
    path('client_update/<client_id>', views.client_update, name='client-update'),
    path('client_delete/<client_id>', views.client_delete, name='client-delete'),
   # dpath('client_update/<tel>', views.client_update, name='client-update'),
]

