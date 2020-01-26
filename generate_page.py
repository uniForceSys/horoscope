# coding: utf-8
from goroscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body):
    text = f'<!doctype html>\n<html lang="ru">\n\n{head}\n{body}</html>'

    return text


def generate_head(title):
    head = '<head>\n<meta charset="UTF-8">\n' \
        '<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, ' \
        'maximum-scale=1.0, minimum-scale=1.0">\n' \
        '<meta http-equiv="X-UA-Compatible" content="ie=edge">\n' \
        f'<title>{title}</title>\n</head>\n'

    return head


def generate_body(header, paragraphs):
    body = f'<h1>{header}</h1>\n'

    for x in paragraphs:
        body += f'<p>\n{x}\n</p>\n'

    return f'<body>\n{body}</body>\n'


def save_page(title, header, list_p):
    fp = open('index.html', 'w')

    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=list_p)
    )

    fp.write(page)
    fp.close()


today = dt.now().date()

save_page(
    title='Гороскоп на сегодня',
    header=f'Что день {str(today)} готовит',
    list_p=generate_prophecies()
)
