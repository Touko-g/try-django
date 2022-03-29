import random

from django.http import HttpResponse
from articles.models import Article


def home(request):
    random_id = random.randint(1, 2)

    article_obj = Article.objects.get(id=random_id)

    h1_string = f"""
        <h1>{article_obj.title}(id:{article_obj.id})</h1>
    """
    p_string = f"""
        <p>{article_obj.content}</p>
    """

    html_string = h1_string + p_string

    return HttpResponse(html_string)
