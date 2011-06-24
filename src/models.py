from google.appengine.ext import db

# String Choices

CATEGORY_KEYS = ['Fixed', 'Mobile'] 
MODE_KEYS = ['Contact', 'Information', 'Invitation', 'Advert'] 

    
class Category(db.Model):
    title = db.StringProperty()
    desc = db.TextProperty()
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class Mode(db.Model):
    title = db.StringProperty()
    desc = db.TextProperty()
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class Service(db.Model):
    title = db.StringProperty()
    desc = db.TextProperty()
    location = db.GeoPtProperty()
    time = db.DateTimeProperty(auto_now_add=True)
    extras = db.TextProperty()
    category = db.StringProperty()
    mode = db.StringProperty(choices=MODE_KEYS)
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
    
class Provider(db.Model):
    user = db.UserProperty()
    FirstName = db.StringProperty()
    LastName = db.StringProperty()
    phone = db.PhoneNumberProperty()
    nickname = db.StringProperty()
    twitter = db.IMProperty()
    facebook = db.IMProperty()
    Services = db.ReferenceProperty(Service, collection_name='Services')
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
