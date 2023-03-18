from django.shortcuts import render
from django.http import HttpResponse


posts = [
        {
        'author': "Администратор",
        "title": "Это первый пост",
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022'
        },
        {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Содержание второго поста.',
        'date_posted': '13 мая, 2022'
        }
        ]


def home(request):
        context = {
        'posts': posts
        }
        return render(request, 'blog/home.html', context)

def about(request):
        return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})
