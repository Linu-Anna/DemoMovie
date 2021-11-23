from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import movie
from.forms import MovieForm
# Create your views here.
def index(request):
    mo=movie.objects.all()
    context={
        'movie_list':mo
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':mov})
def add_movie(request):
    if request.method=='POST':
       name=request.POST.get('name')
       desc = request.POST.get('desc')
       year = request.POST.get('year')
       img= request.FILES['img']
       mov=movie(name=name,desc=desc,year=year,img=img)
       mov.save()

    return render(request,'add.html')
def update(request,id):
    mov=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect ('/')
    return render(request,'edit.html',{'form':form,'movie':mov})
def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request, 'delete.html')