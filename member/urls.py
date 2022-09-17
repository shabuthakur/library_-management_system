from django.urls import path
from member.views import *
from librarian.views import *


urlpatterns = [
   path('get-all-books/',GetAllBooks.as_view()),
   path('book-borrowed/',BorrowBookAPI.as_view()),
   path('return-book/',ReturnBookAPI.as_view()),
   path('delete-member-account/',DeleteMembers.as_view()),

]