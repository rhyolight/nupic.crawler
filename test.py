#!/usr/bin/env python

from random import choice
from nupicrawler import PageFetcher, PageParser, LinkChooser

fetcher = PageFetcher()

def getLinkFrom(url):
  html = fetcher.fetchHtml(url)
  parser = PageParser(html)
  links = parser.getLinks()
  chooser = LinkChooser(url)
  validLinks = chooser.getOtherDomainLinks(links)
  return choice(validLinks)

def crawl(url):
  print url
  link = getLinkFrom(url)
  nextUrl = link["href"]
  try:
    crawl(nextUrl)
  except:
    crawl(url)


url = "http://numenta.com/"

crawl(url)
