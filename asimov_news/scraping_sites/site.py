import requests
from pprint import pprint
from bs4 import BeautifulSoup

class Site:
  def __init__(self, site):
    self.site = site
    self.news = []

  def update_news(self):
    if self.site.lower() == 'globo':
      url = 'https://www.globo.com/'
      browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
      page = requests.get(url, headers=browsers)

      resposta = page.text
      soup = BeautifulSoup(resposta, 'html.parser')
      noticias = soup.find_all('a')

      tg_class1 = 'post__title'
      tg_class2 = 'post-multicontent__link--title__text'

      news_dict_globo = {}

      for noticia in noticias:
        if noticia.h2 != None:
          if tg_class1 in noticia.h2.get('class') or tg_class2 in noticia.h2.get('class'):
            news_dict_globo[noticia.h2.text] = noticia.get('href')
      
      self.news = news_dict_globo
      return self.news



if __name__ == '__main__':
  sites = Site('globo')
  pprint(sites.update_news())