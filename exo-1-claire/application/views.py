from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from .forms import questionform
from django.utils import timezone

def index(request):
    questions=Question.objects.all()
    return render(request, 'application/index.html', {'questions':questions})

def create(request):
    if request.method=="POST":
        text = request.POST['text']
        question = Question.objects.create(text=text)
        question.save()
        return redirect('/')

    return render(request, 'application/create.html')

def edit(request, id):
    question=Question.objects.get(id=id)
    return render(request, 'application/edit.html', {'question':question})

def update(request, id):
    question=Question.objects.get(id=id)
    form = questionform(request.POST, instance=question)
    if form.is_valid:
        form.save()
        return redirect('/')


def delete(request, id):
    Question.objects.filter(id=id).delete()
    return redirect('/')