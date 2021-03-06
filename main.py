import os
import feedparser
from slugify import slugify

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

        # colocar o ultimo item como destaque
        # TODO

        r = slugify(entry.link)

        url = "./" + PORTAL + "/" + r + '.html'

        # atualiza index.html
        index = open("./" + PORTAL + "/" + INDEX, "a")
        index.write("<p> <a href='./" + r + '.html' + "'>" + entry.title + "</a></p>")
        index.close()

        if os.path.exists(url):
            os.remove(url)

        # cria o arquivo da noticia  
        f = open(url, "w+")
        f.write("<br>" + entry.published + "<br>" + entry.summary + "<br>" + entry.description)

        # Adicionar tags google

        # adicionar tag manager google

        f.close()