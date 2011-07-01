'''
Created on Jun 24, 2011

@author: e911miri
'''
from models import Service, Category
import simplejson
import rest
from datetime import datetime
from google.appengine.ext import webapp, gql
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.db import GqlQuery

rest.Dispatcher.base_url = "/apis/rest"
start = datetime.now()
rest.Dispatcher.add_models({
  "svc": Service,
  "cat": Category})

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><h1>this is crap</h1></body></html>')

class Categories(webapp.RequestHandler):
    def get(self):
        cats=[]
        for x in Category.all():
            cats.append(x.to_dict())
        self.response.out.write(simplejson.dumps(cats))

class Browse(webapp.RequestHandler):
    def get(self, category, service):
        svc=Service.get_by_key_name(service)
        self.response.out.write(simplejson.dumps(svc))

class BrowseCat(webapp.RequestHandler):
    def get(self, category):
        query="SELECT * FROM Service WHERE category='"+category+"'"
        svcs=GqlQuery(query)
        svc={}
        for x in svcs:
            svc[x.key()]=x.to_dict()
        self.response.out.write(simplejson.dumps(svc))   
            
class NewService(webapp.RequestHandler):
    def get(self):
        svc_list=[]
        for x in Service.all():
            svc_list.append(x.to_dict())
        self.response.out.write(simplejson.dumps(svc_list))
    def post(self):
        data=self.request.body
        temp=data
        s=Service()
        try:            
            s.category=temp['category']
            s.desc=temp['desc'] 
            s.extras=temp['extras']
            s.location=db.GeoPtProperty(temp['location'])
            s.mode=temp['mode']
            s.title=temp['title']            
        except:
            self.response.out.write('not registered due to technical difficulties')
        if s:
            s.put()
            self.restponse.out.write(s.title)

class SearchHandler(webapp.RequestHandler):
    def get(self):
        pos=self.request.get('position')
        cat=self.request.get('category')
        if pos & cat:
            query="SELECT * FROM Service HERE category='"+ cat + "'"
            

application = webapp.WSGIApplication([('/apis/', MainPage),
                                      ('/apis/svc', NewService),
                                      ('/apis/cat', Categories),
                                      ('/apis/browse/(.*)/(.*)', Browse),
                                      ('/apis/rest/.*', rest.Dispatcher),
                                      ('/apis/browsecat/(.*)', BrowseCat),
                                      ('/apis/search', SearchHandler),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()