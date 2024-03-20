# urls.py
from django.contrib import admin
from django.urls import path
from bibliotheque.views import home_view, add_book_view

from usermanagement.views import add_reader_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('add-reader/', add_reader_view, name='add_reader'),
    path('add-book/', add_book_view, name='add_book'),
   
]
