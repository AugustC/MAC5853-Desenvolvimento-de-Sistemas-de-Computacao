class Restriction():

    def __init__(self, html):
        self.prohibited = False
        self.restrictions = self.try_restriction(html)

    def try_restriction(self, html):
        # Implemented in child classes
        raise NotImplementedError


class RegexRestriction(Restriction):

    def __init__(self, html):
        super().__init__(html)
        self.description = 'Regex restriction'

    def try_restriction(self, html):
        raise NotImplementedError

class ImageRestriction(Restriction):

    def __init__(self, html):
        super().__init__(html)
        self.description = 'Image restriction'

    def try_restriction(self, html):
        raise NotImplementedError


class MLRestriction(Restriction):

    def __init__(self, html):
        super().__init__(html)
        self.description = 'Machine Learning restriction'

    def try_restriction(self, html):
        raise NotImplementedError
