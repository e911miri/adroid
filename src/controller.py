'''
Created on Jun 13, 2011

@author: e911miri
'''
from google.appengine.ext import db

def pages(pages_per_time=10, model):
    if type(model) is db.Model:
        return model.all().count() / pages_per_time
    else:
        return 0

