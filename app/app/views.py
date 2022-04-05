import random

from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home(request, *args, **kwargs):
    random_id = random.randint(1, 2)

    article_obj = Article.objects.get(id=random_id)

    article_list = Article.objects.all()

    context = {
        "article_list": article_list,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id

    }

    # tmpl = get_template('home-view.html').render(context=context)

    html_string = render_to_string('home-view.html', context=context)

    # html_string = """
    #     <h1>{title}(id:{id})</h1>
    #     <p>{content}</p>
    # """.format(**context)

    return HttpResponse(html_string)
