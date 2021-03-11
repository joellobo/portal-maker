import os
import sys
import logging

import feedparser
from slugify import slugify
from google_trans_new import google_translator

PORTAL = "site"
INDEX = "index.html"

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def main():
    update_site()


def update_site():
    logging.debug("executando metodo update_site")

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

            translator = google_translator()

            noticia = {
                "titulo": translator.translate(entry.title, lang_tgt='en'),
                "resumo": translator.translate(entry.summary, lang_tgt='en'),
                "materia": translator.translate(entry.description, lang_tgt='en')
            }

            # colocar o ultimo item como destaque
            # TODO

            r = slugify(entry.link)

            url = "./" + PORTAL + "/" + r + '.html'

            # atualiza index.html
            index = open("./" + PORTAL + "/" + INDEX, "a")
            index.write("<p> <a href='./" + r + '.html' +
                        "'>" + noticia["titulo"] + "</a></p>")
            index.close()

            # gerar a patir de um template
            # TODO

            if not os.path.exists(url):
                #os.remove(url)

                # cria o arquivo da noticia
                f = open(url, "w+")

                f.write(noticia["titulo"] + "<br>" + entry.published + "<br>" +
                        noticia["resumo"] + "<br>" + noticia["materia"])

                # Adicionar tags google

                # adicionar tag manager google

                # adicionar noticias relacionadas

                f.close()

                # upload s3 / digitalocean
                # TODO

                # Publicar nas redes sociais twitter/facebook/instagram
                # TODO


if __name__ == '__main__':
    main()
