from django.contrib import admin
from django.urls import path
from bibliotheque import views 
from usermanagement.views import add_reader_view, afficher_lecteurs, afficher_livres
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('add-reader/', add_reader_view, name='add_reader'),
    path('add-book/', views.add_book_view, name='add_book'),
    path('erreur/', views.error_page, name='error_page'),
    path('succes/', views.success_page, name='success_page'),
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/<int:livre_id>/edit/', views.edit_livre, name='edit_livre'),
    path('livres/pret/<int:livre_id>/', views.pret, name='pret'),

    # Nouvelle URL pour afficher les lecteurs
    path('lecteurs/', afficher_lecteurs, name='afficher_lecteurs'),
    path('lecteurs/<str:username>/livres/', afficher_livres, name='afficher_livres'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
