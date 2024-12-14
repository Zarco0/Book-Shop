from django import forms
from .models import tbl_Book,tbl_Author

class AuthorForm(forms.ModelForm):

    class Meta:

        model=tbl_Author
        fields=['name']

class BookForm(forms.ModelForm):

    class Meta:

        model=tbl_Book
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book name'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Enter the author name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the book price'}),
        }