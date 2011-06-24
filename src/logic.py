'''
Created on Jun 22, 2011

@author: e911miri
'''
from google.appengine.api import users

from models import Provider
from google.appengine.ext.db import GqlQuery


def userexists(user):
    allusers = GqlQuery('SELECT user FROM Provider')
    if user in allusers:
        return True
    else:
        return False
    
def getProvider(user):
    prov = GqlQuery('SELECT __key__ FROM Provider WHERE user={0}', user)
    for x in prov:
        return (x.__key__)
