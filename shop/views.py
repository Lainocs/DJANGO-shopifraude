from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    return render(request, 'shop/index.html', {
        'articles': Article.objects.filter(quantity__gt=0)
    })

def create(request):
    context = {}
    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
    context['form']= form
    return render(request, 'shop/create.html', context)

def buy(request, article_id):
    # remove 1 from quantity
    article = get_object_or_404(Article, pk=article_id)
    article.quantity -= 1
    article.save()
    return HttpResponseRedirect('/')

# def edit(request, article_id):
#     context = {}
    
#     obj = get_object_or_404(Article, id=article_id)
    
#     form = ArticleForm(request.POST or None, instance=obj)
    
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/')
    
#     context["form"] = form
    
#     return render(request, "shop/edit.html", context)

def detail(request, article_id):
    return render(request, 'shop/detail.html', {
        'article': Article.objects.get(id=article_id)
    })