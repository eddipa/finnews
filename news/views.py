'''
news.views.py
'''
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator 
from .tasks import update_all_feeds
from feeds.models import Source, Post

def index(request):
    """
    Renders the index page listing all feed sources.
    """
    # Optionally: trigger a background feed refresh (disabled by default)
    # update_all_feeds.delay(10)

    # Retrieve all sources and prefetch related posts for template efficiency
    sources = Source.objects.prefetch_related('posts').all()

    context = {
        'source_list': sources,
    }
    return render(request, 'news/index.html', context)


def source_detail(request, source_id):
    """
    Renders the detail page for a specific news source and its paginated posts.
    """
    # Attempt to fetch the source by ID, or return 404
    source = get_object_or_404(Source, id=source_id)

    # Get all related posts for this source
    posts = source.posts.all()

    # Paginate the post list (10 posts per page)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'source': source,
        'posts': page_obj,
    }
    
    return render(request, 'news/source.html', context)


