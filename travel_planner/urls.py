from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('voyage/<int:voyage_id>/', views.detail_voyage, name='detail_voyage'),
    path('liste_voyages/', views.liste_voyages, name='liste_voyages'),
    path('search_voyage/', views.search_voyage, name='search_voyage'),
    path('liste_hebergements/', views.liste_hebergements, name='liste_hebergements'),
    path('search_hebergement/', views.search_hebergement, name='search_hebergement'),
    path('detail_hebergement/<int:hebergement_id>/', views.detail_hebergement, name='detail_hebergement'),
    path('search_destination/', views.search_destination, name='search_destination'),
    path('destination/', views.destination, name='destination'),
    path('ajouter_reservation_hebergement/<int:hebergement_id>/', views.ajouter_reservation_hebergement, name='ajouter_reservation_hebergement'),
    path('choix_reservation/', views.choix_reservation, name='choix_reservation'),
    path('mes_reservations_voyages/', views.mes_reservations_voyages, name='mes_reservations_voyages'),
    path('mes_reservations_hebergements/', views.mes_reservations_hebergements, name='mes_reservations_hebergements'),
    path('reservation_voyage/<int:voyage_id>/', views.detail_reservation_voyage, name='reservation_voyage'),
    path('reservation_hebergement/<int:hebergement_id>/', views.detail_reservation_hebergement, name='reservation_hebergement'),
    path('supprimer_reservation/<int:reservation_id>/', views.supprimer_reservation, name='supprimer_reservation'),
    path('ajouter_reservation_voyage/<int:voyage_id>/', views.ajouter_reservation_voyage, name='ajouter_reservation_voyage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("", views.index, name="index"),
]