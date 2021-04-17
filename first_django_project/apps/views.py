from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request) :
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request) :
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request) :
    return redirect('/')

def show(request,number) :
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request,number) :
    return HttpResponse(f'placeholder to edit blog: {number}')

def destroy(request,num) :
    return redirect('/blogs')

def root(request) :
    return redirect('/blogs')

def showJson(request) :
    return JsonResponse({"title": "My first blog", "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit"})
