from django.shortcuts import render, redirect
from .models import *
from .forms import AddTovar
# Create your views here.


def index(request):
    tovars = Tovar.objects.all()
    return render(request, 'index.html', context={'tovars': tovars})


def info(request):
    try:
        tovar = Tovar.objects.get(id=id)
        return render(request, 'tovar.html', context={'tovar': tovar})
    except:
        return redirect('index')


def create(request):

    if request.method == 'POST':

        form = AddTovar(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            sell = form.cleaned_data['sell']
            

            Tovar.objects.create(title=title, sell=sell)
            return redirect('index')

        else:

            form = AddTovar()
            return render(request, 'create.html', context={'form': form})

    else:

        form = AddTovar()
        return render(request, 'create.html', context={'form': form})


def delete(request, id):
    try:
        tovar = Tovar.object.get(id=id)
        return render('index')
    except:
        return redirect('index')




