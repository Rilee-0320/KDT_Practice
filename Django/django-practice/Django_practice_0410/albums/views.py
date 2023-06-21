from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums:create')
    else:
        form = AlbumForm()
    albums = Album.objects.all()
    context = {
        'form': form,
        'albums': albums,
    }
    return render(request, 'albums/create.html', context)