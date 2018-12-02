import re
import json

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
        count = 0
        with open('flaskr/restrictions.json', 'r') as f:
            restrictions = json.loads(f.read())
        regex = restrictions['regular_expressions']
        patterns_found = []
        for pattern in regex:
            matches = re.findall(pattern, html.lower(), flags=re.IGNORECASE)
            count += len(matches)
            patterns_found.append(pattern)
        if count > 10:
            self.prohibited = True
        else:
            self.prohibited = False
        return patterns_found

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
