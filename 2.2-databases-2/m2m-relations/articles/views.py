from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    data = Article.objects.all()
    context = {
        'object_list': data,
    }

    return render(request, template, context)
