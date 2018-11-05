from . import db
from datetime import datetime

class MURL(db.Model):
    __tablename__ = 'URL'

    id = db.Column(db.Integer, primary_key=True)
    urlpath = db.Column(db.String(255), unique=True)

    def __init__(self, urlpath):
        self.urlpath = urlpath

    def __repr__(self):
        return f"URL is {self.urlpath}"

class MPROHIBITIONTYPE(db.Model):
    __tablename__ = 'PROHIBITIONTYPE'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Prohibition Type is {self.description}"

class MSTATUSTYPE(db.Model):
    __tablename__ = 'STATUSTYPE'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Status Type is {self.description}"

class MRESTRICTION(db.Model):
    __tablename__ = 'RESTRICTION'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Restriction is {self.description}"

class MREGEXRESTRICTION(db.Model):
    __tablename__ = 'REGEXRESTRICTION'

    id = db.Column(db.Integer, primary_key=True)
    restriction_id = db.Column(db.Integer,db.ForeignKey('RESTRICTION.id'))
    regex_rule = db.Column(db.String(255))

    def __init__(self,restriction_id, regex_rule):
        self.restriction_id = restriction_id
        self.regex_rule = regex_rule

    def __repr__(self):
        return f"Regex Restriction is {self.regex_rule}"

class MMACHINELEARNINGR(db.Model):
    __tablename__ = 'MACHINELEARNINGR'

    id = db.Column(db.Integer, primary_key=True)
    restriction_id = db.Column(db.Integer,db.ForeignKey('RESTRICTION.id'))
    model_path = db.Column(db.String(255))

    def __init__(self,restriction_id, regex_rule):
        self.restriction_id = restriction_id
        self.model_path = model_path

    def __repr__(self):
        return f"Machine Learning Restriction is {self.model_path}"

class MIMAGERESTRICTION(db.Model):
    __tablename__ = 'IMAGERESTRICTION'

    id = db.Column(db.Integer, primary_key=True)
    restriction_id = db.Column(db.Integer,db.ForeignKey('RESTRICTION.id'))
    image_rule = db.Column(db.String(255))

    def __init__(self,restriction_id, image_rule):
        self.restriction_id = restriction_id
        self.image_rule = image_rule

    def __repr__(self):
        return f"Image Restriction is {self.image_rule}"

class MURLPROCESSMENT(db.Model):
    __tablename__ = 'URLPROCESSMENT'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer,db.ForeignKey('URL.id'))
    status_id = db.Column(db.Integer,db.ForeignKey('STATUSTYPE.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,url_id, status_id, date_created):
        self.url_id = url_id
        self.status_id = status_id
        self.date_created = date_created

    def __repr__(self):
        return f"Url processment created on {self.date_created}"



class MURLPROHIBITION(db.Model):
    __tablename__ = 'URLPROHIBITION'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer,db.ForeignKey('URL.id'))
    prohibition_id = db.Column(db.Integer,db.ForeignKey('PROHIBITIONTYPE.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,url_id, prohibition_id, date_created):
        self.url_id = url_id
        self.prohibition_id = prohibition_id
        self.date_created = date_created

    def __repr__(self):
        return f"Url Prohibition created on {self.date_created}"


class MREASONSPROHIBITION(db.Model):
    __tablename__ = 'REASONSPROHIBITION'

    id = db.Column(db.Integer, primary_key=True)
    url_processment_id = db.Column(db.Integer, db.ForeignKey('URLPROCESSMENT.id'))
    restriction_id = db.Column(db.Integer,db.ForeignKey('RESTRICTION.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    url_id = db.Column(db.Integer, db.ForeignKey('URL.id'))

    def __init__(self,url_processment_id, restriction_id, date_created, url_id):
        self.url_processment_id = url_processment_id
        self.restriction_id = restriction_id
        self.date_created = date_created
        self.url_id =url_id

    def __repr__(self):
        return f"Reasons Prohibition created on {self.date_created}"
