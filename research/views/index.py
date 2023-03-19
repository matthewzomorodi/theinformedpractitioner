from django.shortcuts import render


def index(request):
    context = {
        'index_title': 'Research Home Page',
    }
    return render(request, 'research/index.html', context)