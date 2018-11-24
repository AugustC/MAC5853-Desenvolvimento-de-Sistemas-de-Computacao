from . import db, create_app
from datetime import datetime
from .restrictions import RegexRestriction, ImageRestriction, MLRestriction
from .utils import get_html

class MURL(db.Model):
    __tablename__ = 'URL'

    id = db.Column(db.Integer, primary_key=True)
    urlpath = db.Column(db.String(255), unique=True)

    def __init__(self, urlpath):
        self.urlpath = urlpath

    def __repr__(self):
        return f"URL is {self.urlpath}"

    def serialize(self):
        return {
            'id': self.id,
            'urlpath': self.urlpath,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MURL.query.all()

class MPROHIBITIONTYPE(db.Model):
    __tablename__ = 'PROHIBITIONTYPE'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Prohibition Type is {self.description}"

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MPROHIBITIONTYPE.query.all()

class MSTATUSTYPE(db.Model):
    __tablename__ = 'STATUSTYPE'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Status Type is {self.description}"

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def setWaiting(self):
        self.description = 'Not Processed'
        self.save()

    def setProcessing(self):
        self.description = 'Processing'
        self.save()

    def setEnded(self):
        self.description = 'Processed'
        self.save()

    @staticmethod
    def get_all():
        return MSTATUSTYPE.query.all()

class MRESTRICTION(db.Model):
    __tablename__ = 'RESTRICTION'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Restriction is {self.description}"

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MRESTRICTION.query.all()

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MREGEXRESTRICTION.query.all()

class MMACHINELEARNINGR(db.Model):
    __tablename__ = 'MACHINELEARNINGR'

    id = db.Column(db.Integer, primary_key=True)
    restriction_id = db.Column(db.Integer,db.ForeignKey('RESTRICTION.id'))
    model_path = db.Column(db.String(255))

    def __init__(self,restriction_id, model_path):
        self.restriction_id = restriction_id
        self.model_path = model_path

    def __repr__(self):
        return f"Machine Learning Restriction is {self.model_path}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MMACHINELEARNINGR.query.all()

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MIMAGERESTRICTION.query.all()

class MURLPROCESSMENT(db.Model):
    __tablename__ = 'URLPROCESSMENT'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer,db.ForeignKey('URL.id'))
    status_id = db.Column(db.Integer,db.ForeignKey('STATUSTYPE.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,url_id, status_id, date_created=datetime.utcnow()):
        self.url_id = url_id
        self.status_id = status_id
        self.date_created = date_created

    def __repr__(self):
        return f"Url processment created on {self.date_created}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def startProcessing(self):
        self.processRestriction()

    def processRestriction(self):
        status = MSTATUSTYPE.query.get(self.status_id)
        status.setProcessing()
        url = MURL.query.get(self.url_id)
        print('Processing', url)
        html = get_html(url.urlpath)
        regex_restriction = RegexRestriction(html)
        #image_restriction = ImageRestriction(html)
        #ml_restriction = MLRestricion(html)
        self.setProhibition(regex_restriction)
        #self.setProhibition(image_restriction)
        #self.setProhibition(ml_restriction)
        status.setEnded()

    def setProhibition(self, restriction):
        if not restriction.prohibited:
            print("Not prohibited")
            pass
        else:
        # Create ReasonsProhibition, create URLProhibition
            print("Prohibited")
            pass

    @staticmethod
    def get_all():
        return MURLPROCESSMENT.query.all()

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MURLPROHIBITION.query.all()

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return MREASONSPROHIBITION.query.all()
