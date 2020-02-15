from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def view_article(request, id):
    obj = get_object_or_404(Article, id=id)
    return render(request,
        template_name = 'article/article.html',
        context={'object': obj}
    )
