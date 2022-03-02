from django import forms
from .models import Article
 
# creating a form
class ArticleForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Article
 
        # specify fields to be used
        fields = [
            'title',
            'image',
            'description',
            'price',
            'quantity',
        ]