import rest, ast
import simplejson
from datetime import datetime
from google.appengine.api import users, oauth
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Service, Category

rest.Dispatcher.base_url = "/rest"
start=datetime.now()
rest.Dispatcher.add_models({
  "svc": Service,
  "cat": Category})
class MainHandler(webapp.RequestHandler):
    def get(self):
        req=self.request
        cats=Category.all()
        svcs=Service.all()
        self.response.out.write(simplejson.dumps([p.to_dict() for p in svcs]))
    def post(self):
        request=self.request      
        self.response.out.write(dict(ast.literal_eval(request.body))['name'])

class CatHandler(webapp.RequestHandler):
    def get(self):
        categories=Category.all()           
        self.response.out.write(simplejson.dumps([p.to_dict() for p in categories]))    
    def post(self):
        user= users.get_current_user()
        if user:
            req=dict(ast.literal_eval(self.request.body))
            try:
                title=req['title']
            except:
                pass
            try:
                desc=req['title']
            except:
                pass
            c=Category()
            c.title=title
            c.desc=desc
            c.put()
            self.response.out.write(simplejson.dumps(c.to_dict()))  
        else:
            self.redirect(users.create_login_url('/login'))

class Search(webapp.RequestHandler):
    pass


class Svc(webapp.RequestHandler):
    pass


class Unregister(webapp.RequestHandler):
    pass


      
def main():
    application = webapp.WSGIApplication(
          [('/', MainHandler),
           ('/cat', CatHandler),
           ('/rest/.*', rest.Dispatcher)
          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()