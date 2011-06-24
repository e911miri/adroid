import rest, os
import webapp2
import simplejson
import logic
from datetime import datetime
from google.appengine.api import users, oauth
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Service, Category, Provider
from google.appengine.ext.db import GqlQuery

#
# Default Rest Service
#
rest.Dispatcher.base_url = "/rest"
start = datetime.now()
rest.Dispatcher.add_models({
  "svc": Service,
  "cat": Category})

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {}
        template_path = os.path.join(os.path.dirname(__file__), "templates/index.html")
        template_values['svc'] = Service.all()
        template_values['cat'] = Category.all()
        self.response.out.write(template.render(template_path, template_values))
    def post(self):
        request = self.request

class CatHandler(webapp.RequestHandler):
    def get(self):        
        cat=[]
        for x in Category.all():
            cat.append(x.to_dict())
        self.response.out.write(simplejson.dumps(cat))
#    
#    def get(self):
#        template_path = os.path.join(os.path.dirname(__file__), 'templates/categories.html')
#        template_values = {'cat': Category.all()}
#        self.response.out.write(template.render(template_path, template_values))
#    def post(self):
#        try:
#            title = self.request.get('title')
#            desc = self.request.get('desc')
#        except:
#            self.redirect('/categories')
#        if title:
#            c = Category(title=title, desc=desc)
#            c.put()
#        self.redirect('/categories')

class Search(webapp.RequestHandler):
    def get(self):
        radius = self.request.get('radius')
        longitude = self.request.get('longitude')
        latitude = self.request.get('latitude')
        category = self.request.get('category')
        query = 'SELECT * FROM Service WHERE category=' + category
        cat_dict = {}
        cat = GqlQuery(query)
        for c in cat:
            cat_dict[c.title] = c.desc             
        from webapp2_extras import json        
        self.response.out.write(json.json.dump(cat_dict))

class BrowseServices(webapp.RequestHandler):
    def get(self):
        pass

class Register(webapp.RequestHandler):
    def get(self, category, service_key):
        
        pass
    def post(self):
        user = users.get_current_user()
        if user:
            prov = Provider.all().filter('user =', user)
            prov[0] = {}
                
            
class Svc(webapp.RequestHandler):
    pass

class Unregister(webapp.RequestHandler):
    pass
      
def main():
    application = webapp2.WSGIApplication(
          [('/', MainHandler),
           (r'/browse/(.*)/(.*)', BrowseServices),
           ('/categories', CatHandler),
           ('/rest/.*', rest.Dispatcher)
          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
