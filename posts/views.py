from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    
    context ={
        'form' : form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)
    user1 = post.select1_users.all()
    user2 = post.select2_users.all()
    if request.user not in user1 and request.user not in user2:
        if answer == 'select1':
            post.select1_users.add(request.user)
        elif answer == 'select2':
            post.select2_users.add(request.user)


    # post.save()
    return redirect('posts:detail', post.pk)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post':post,
    }
    return render(request, 'posts/detail.html', context)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')



