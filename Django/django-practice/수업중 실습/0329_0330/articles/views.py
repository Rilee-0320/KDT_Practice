from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)