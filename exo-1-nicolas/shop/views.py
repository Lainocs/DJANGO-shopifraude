from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from .forms import QuestionForm
from django.utils import timezone

def index(request):
    return render(request, 'shop/index.html', {'questions': Question.objects.all()})

def detail(request, id):
    return render(request, 'shop/detail.html', {
        'question': Question.objects.get(id=id)
    })
    
def create(request):
    context = {}
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
    context['form']= form
    return render(request, 'shop/create.html', context)

def edit(request, id):
    context = {}
    
    obj = get_object_or_404(Question, id=id)
    
    form = QuestionForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context["form"] = form
    
    return render(request, "shop/edit.html", context)

def delete(request, id):
    context ={}

    obj = get_object_or_404(Question, id = id)

    if request.method =="POST":
        
        obj.delete()
        
        return HttpResponseRedirect("/")

    return render(request, "shop/delete.html", context)
# Create your views here.
