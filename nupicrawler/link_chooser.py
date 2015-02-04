from random import choice
from urlparse import urlparse

class LinkChooser(object):

  def __init__(self, url):
    self._url = urlparse(url)
    print self._url.hostname

  def _isNewDomain(self, url):
    return self._url.hostname != url.hostname

  def getOtherDomainLinks(self, links):
    otherDomainLinks = []
    for link in links:
      href = link["href"]
      if href[:4] == "http":
        url = urlparse(href)
        if self._isNewDomain(url):
          otherDomainLinks.append(link)
    return otherDomainLinks

  def chooseOne(self, links):
    return choice(self.getOtherDomainLinks(links))