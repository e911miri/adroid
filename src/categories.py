'''
Created on Jun 22, 2011

@author: e911miri
'''
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template
from models import Category
class MainHandler(webapp.RequestHandler):
    def get(self):
#        template_values={}
#        template_path=os.path.join(os.path.dirname(__file__),"templates/categories.html")
#        template_values['cat']=Category.all()
#        self.response.out.write(template.render(template_path, template_values))
        self.response.out.write("I got here")
    

def main():
    application = webapp2.WSGIApplication(
          [('/', MainHandler),
          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
