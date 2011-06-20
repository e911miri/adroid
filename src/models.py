from google.appengine.ext import db

# String Choices

CATEGORY_KEYS = ['Fixed', 'Mobile'] 
MODE_KEYS=['Contact', 'Information', 'Invitation', 'Advert'] 

    
class Category(db.Model):
    title=db.StringProperty()
    desc=db.TextProperty()
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class Mode(db.Model):
    title=db.StringProperty()
    desc=db.TextProperty()

class Service(db.Model):
    title=db.StringProperty()
    desc=db.TextProperty()
    location=db.GeoPtProperty()
    time=db.DateTimeProperty(auto_now_add=True)
    extras=db.TextProperty()
    category = db.StringProperty(choices=CATEGORY_KEYS)    
    client=db.UserProperty(auto_current_user_add=True)
    mode=db.StringProperty(choices=MODE_KEYS)
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
    
class Provider(db.Model):
    user=db.UserProperty()
    FirstName=db.StringProperty()
    LastName=db.StringProperty()
    Services=db.ReferenceProperty(Service, collection_name='Services')