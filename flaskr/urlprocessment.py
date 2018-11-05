from utils import get_html
import datetime
from flaskr import RegexRestriction, ImageRestriction
from flaskr import statusType

class URLProcessment():

    def __init__(self, url):
        self.url = url
        self.date_created = datetime.datetime.now()
        status = statusType()
        self.status = status.setWaiting()
        self.prohibition = None

    def processRestriction(self, url):
        self.status.setProcessing()
        html = get_html(url)

        regex_restriction = RegexRestriction(html)
        image_restriction = ImageRestriction(html)
        ml_restriction = MLRestricion(html)
        self.setProhibition(regex_restriction)
        self.setProhibition(image_restriction)
        self.setProhibition(ml_restriction)

        self.status.setEnded()

    def setProhibition(self, restriction):
        if not restriction.prohibited:
            return
        else:
        # Create ReasonsProhibition, create URLProhibition
            pass
