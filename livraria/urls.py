from django.urls import path
from livraria.views import (
    home, 
    logout_user, 
    register, 
    book_detail, 
    book_delete,
    add_book,
    book_update
)

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name = "logout"),
    path('register/', register, name = "register"),
    path('book/<int:id>', book_detail, name = "book"),
    path('delete_book/<int:id>', book_delete, name="delete_book"),
    path('add_book/', add_book, name="add_book"),
    path('update_book/<int:id>', book_update, name="update_book")
]
