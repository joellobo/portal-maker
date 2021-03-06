import os
import feedparser
from slugify import slugify
from translate import Translator

PORTAL = "site"
INDEX = "index.html"

# ler os links dos feeds
feed_sources = open('sources.txt', 'r')
Lines = feed_sources.readlines()

count = 0
for line in Lines:
    count += 1

    feed = feedparser.parse(line.strip())

    total = len(feed['entries'])

    for i in range(1, total):
        entry = feed.entries[i]

        conf = Translator(from_lang='pt-br', to_lang='english')

        noticia = {
            "titulo": conf.translate(entry.title),
            "resumo": conf.translate(entry.summary),
            "materia": conf.translate(entry.description)
        }

        # TODO
        # colocar o ultimo item como destaque

        r = slugify(entry.link)

        url = "./" + PORTAL + "/" + r + '.html'

        # atualiza index.html
        index = open("./" + PORTAL + "/" + INDEX, "a")
        index.write("<p> <a href='./" + r + '.html' +
                    "'>" + noticia["titulo"] + "</a></p>")
        index.close()

        if os.path.exists(url):
            os.remove(url)

        # cria o arquivo da noticia
        f = open(url, "w+")

        # traduzir

        f.write("<br>" + entry.published + "<br>" +
                noticia["resumo"] + "<br>" + noticia["materia"])

        # Adicionar tags google

        # adicionar tag manager google

        f.close()
