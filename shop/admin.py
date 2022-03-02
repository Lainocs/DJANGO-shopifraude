from django.contrib import admin

# Register your models here.
from shop.models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'image',
        'description',
        'price',
        'quantity',
        'created_at',
        'updated_at',
    ]
    
admin.site.register(Article)