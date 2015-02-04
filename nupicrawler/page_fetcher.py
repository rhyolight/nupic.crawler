import requests

class PageFetcher(object):

  def __init__(self):
    pass


  def fetchHtml(self, url):
    header = requests.head(url)
    if "text/html" not in header.headers["content-type"]:
      raise Exception("Bad content-type")
    response = requests.get(url)
    return response.content