from django.urls import path
from .import views

app_name = 'webbook'

urlpatterns = [
    path('createBook',views.BookCreate,name="createbook"),
    path('',views.listBook,name='listview'),
    path('author/',views.AuthorCreate,name='author'),
    path('details/<int:book_id>/',views.BookDetails,name='detailss'),
    path('update/<int:book_id>/',views.BookUpdate,name='update'),
    path('delete/<int:book_id>/',views.BookDelete,name='delete'),
    path('index/',views.index),
    path('search/',views.SearchBook,name='search'),
    
]