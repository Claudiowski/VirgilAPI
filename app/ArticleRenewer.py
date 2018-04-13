from .models import StreamDao, ArticleDao

import requests, time

from threading import Thread


class ArticleRenewer(Thread):
    """ Thread that loads consultable articles in database, using rss2json web service. """
    
    rss2json_url = 'https://api.rss2json.com/v1/api.json'
    streams = []

    def __init__(self, session):
        
        self.session = session
        Thread.__init__(self)

    def load_streams(self):
        """ Renew stream list. """
        
        self.streams = self.session.query(StreamDao).all()

    def load_articles(self):
        """ Loads all articles from rss links. """

        articles = []
        
        for s in self.streams:
                        
            payload = { 'rss_url': s.url }
            resp = requests.get(self.rss2json_url, params=payload)

            for item in resp.json()['items']:
                articles.append(ArticleDao(title=item['title'], publication_date=item['pubDate'],\
                                           description=item['description'], url=item['link'], id_stream=s.id))

        self.session.add_all(articles)
        self.session.commit()

    def run(self):
        """ Runs the thread. """
        
        while True:
                        
            self.session.query(ArticleDao).delete()

            self.load_streams()
            self.load_articles()

            time.sleep(5)         

