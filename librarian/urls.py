from django.urls import path
from librarian.views import *


urlpatterns = [
    path('get-all-books/', GetAllBooks.as_view()),
    path('add-books/', AddBooks.as_view()),
    path('update-books-data/', UpdateBook.as_view()),
    path('delete-book/', DeleteBooks.as_view()),
    path('get-all-members/', GetAllMembers.as_view()),
    path('add-member/', AddMembers.as_view()),
    path('update-member/', UpdateMembersData.as_view()),
    path('delete-member/', DeleteMember.as_view()),
]
