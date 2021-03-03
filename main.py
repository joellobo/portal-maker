import feedparser
from slugify import slugify

folder = "./site"

file1 = open('sources.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
  count += 1

  NewsFeed = feedparser.parse(line.strip())
  
  total = len(NewsFeed['entries'])
  
  for i in range(1, total):
    entry = NewsFeed.entries[i]
    r = slugify(entry.link)
    f = open(folder + "/" + r + '.html', "a")
    f.write(entry.published + "\n" + entry.summary)
    
    
    # Adicionar tags google
    
    # adicionar tag manager google
    f.close()

    # get the feed
    #print()
    #print("******")
    #print()
    #print("------News Link--------")
    #print(entry.link)

  # convert to html




