from django.shortcuts import render
from todoapp.models import ListItem
from todoapp.forms import TodoForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):

    list_items = ListItem.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST or None) # so it doesnt raise validation errors before user has submitted
        if form.is_valid():
            form.save(commit=True) # saves form input to database
            return render(request, 'index.html', {'list_items': list_items, 'form': form})
        else:
            print (form.errors)


    return render(request, 'index.html', {'list_items': list_items, 'form': form}) 


def post_remove(request, pk):
    post = get_object_or_404(ListItem, pk=pk)
    post.delete()
    return HttpResponseRedirect('/')
