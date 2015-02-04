from bs4 import BeautifulSoup

class PageParser(object):

  def __init__(self, html):
    self._html = html
    self._soup = BeautifulSoup(html)


  def getLinks(self):
    soup = self._soup
    links = []
    for link in soup.find_all('a'):
      href = link.get("href")
      text = link.string
      if href is not None and text is not None:
        links.append({
          "href": href,
          "text": text
        })
    return links
