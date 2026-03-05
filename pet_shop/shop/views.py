from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Главная страница с ссылками"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Магазин аксессуаров для домашних животных</title>
        <meta charset="utf-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 15px 0;
            }
            a {
                display: inline-block;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            a:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать в магазин аксессуаров для домашних животных!</h1>
        <p>Выберите раздел:</p>
        <ul>
            <li><a href="/about/">О магазине</a></li>
            <li><a href="/author/">Об авторе</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def about_shop(request):
    """Страница о магазине"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>О магазине</title>
        <meta charset="utf-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }
            .back-link {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 16px;
                background-color: #666;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>О нашем магазине</h1>
        <h2>Магазин аксессуаров для домашних животных</h2>
        <p>Тема лабораторной работы: Разработка веб-приложения для магазина аксессуаров домашних животных с использованием Django</p>
        <p>В нашем магазине вы найдете:</p>
        <ul>
            <li>Лежанки и домики для кошек и собак</li>
            <li>Миски и поилки</li>
            <li>Игрушки для активных питомцев</li>
            <li>Одежда для маленьких пород</li>
            <li>Когтеточки и комплексы для кошек</li>
            <li>Транспортировочные сумки и переноски</li>
        </ul>
        <a href="/" class="back-link">Вернуться на главную</a>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def about_author(request):
    """Страница об авторе"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Об авторе</title>
        <meta charset="utf-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }
            .back-link {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 16px;
                background-color: #666;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Об авторе</h1>
        <p><strong>Лабораторную работу выполнил:</strong></p>
        <ul>
            <li>Студент: Данильчик Елизавета</li>
            <li>Группа: 88ТП</li>
            <li>Курс: 2 курс</li>
            <li>Дата выполнения: 05.03.2026</li>
        </ul>
        <p><strong>О себе:</strong></p>
        <p>Крутой студент очень прям вау</p>
        <a href="/" class="back-link">Вернуться на главную</a>
    </body>
    </html>
    """
    return HttpResponse(html_content)