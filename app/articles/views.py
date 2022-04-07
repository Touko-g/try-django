from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


# Create your views here.

def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.get(id=query)
    context = {
        "object": qs
    }
    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # return redirect("article-detail", slug=article_object.slug)
        return redirect(article_object.get_absolute_url())
        # context['object'] = article_object
        # context['created'] = True
    return render(request, "articles/create.html", context=context)


# def article_create_view(request):
#     form = ArticleForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         title = form.cleaned_data.get('title')
#         content = form.cleaned_data.get('content')
#         article_object = Article.objects.create(title=title, content=content)
#         context['object'] = article_object
#         context['created'] = True
#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj
    }

    return render(request, "articles/detail.html", context=context)
