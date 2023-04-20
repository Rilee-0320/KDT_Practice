from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm
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
        form = PostForm(request.POST, request.FILES)
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
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        'post':post,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')


def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:detail', post.pk)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


# @login_required
# def comment_create(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.post = post
#         comment.user = request.user
#         comment.save()
#         return redirect('posts:detail', post.pk)
#     context = {
#         'post': post,
#         'comment_form': comment_form,
#     }
#     return render(request, 'posts/detail.html', context)