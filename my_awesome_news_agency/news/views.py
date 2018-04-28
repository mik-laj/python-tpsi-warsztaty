from django.shortcuts import render


def first_view():
    context = {'hello': 'World'}
    return render(request, 'news/index.html', context)
