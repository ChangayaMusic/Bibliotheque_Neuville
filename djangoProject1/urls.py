from django.contrib import admin
from django.urls import path
from bibliotheque import views 
from usermanagement.views import add_reader_view
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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
