from django.shortcuts import render
from .utils import search_word


def home(request):
    return render(request, 'core/index.html', {})


def search(request):
    query = request.GET['q']
    results = []
    if len(query.strip()) != 0:
        results = search_word(query)
    return render(request, 'core/results.html', {'data': results, 'query': query})
