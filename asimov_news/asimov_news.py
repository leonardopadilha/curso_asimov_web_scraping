from scraping_sites.site import Site
from scraping_sites import *
import os
from threading import Thread
import time
from datetime import datetime
import sys
import pickle
import webbrowser
from math import ceil
from pytimedinput import timedInput

class AsimovNews:
  def __init__(self):
    self.dict_site = {}
    self.all_sites = ['veja', 'r7', 'cnn', 'globo']

    self.screen = 0
    self.kill = False

    self.news = self._read_file('news') if 'news' in os.listdir() else []
    self._update_file(self.news, 'news')
    
    self.sites = self._read_file('sites') if 'sites' in os.listdir() else []
    self._update_file(self.sites, 'sites')

    for site in self.all_sites:
      self.dict_site[site] = Site(site)

    self.news_thread = Thread(target=self.update_news, daemon=True)
    #self.news_thread.setDaemon(True)
    self.news_thread.start()

  def _update_file(self, lista, mode='news'):
    with open(mode, 'wb') as fp:
      pickle.dump(lista, fp)

  def _read_file(self, mode='news'):
    with open(mode, 'rb') as fp:
      n_list = pickle.load(fp)
      return n_list

  def update_news(self):
    while not self.kill:
      for site in self.all_sites:
        self.dict_site[site].update_news()

        for key, value in self.dict_site[site].news.items():
          dict_aux = {}
          dict_aux['data'] = datetime.now()
          dict_aux['fonte'] = site
          dict_aux['materia'] = key
          dict_aux['link'] = value

          if len(self.news) == 0:
            self.news.insert(0, dict_aux)
            continue

          add_news = True
          for news in self.news:
            if dict_aux['materia'] == news['materia'] and dict_aux['fonte'] == news['fonte']:
              add_news = False
              break

            if add_news:
              self.news.insert(0, dict_aux)

      self.news = sorted(self.news, key=lambda d: d['data'], reverse=True)
      self._update_file(self.news, 'news')
      time.sleep(10)
