import feedparser
import json
import pprint

url = 'https://news.google.com/news/rss/search/section/q/%e3%83%88%e3%82%a4%e3%83%ac?ned=jp&hl=ja&gl=JP'

d = feedparser.parse(url)
news = list()

for i, entry in enumerate(d.entries, 1):

    p = entry.published_parsed
    sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)

    tmp = {
        "no": i,
        "title": entry.title,
        "link": entry.link,
        "published": entry.published,
        "sortkey": sortkey
    }

    news.append(tmp)

news = sorted(news, key=lambda x: x['sortkey'])

pprint.pprint(news)