import re

UNWANTED_TERMS_IN_COURSE = ["(\([S,F])([0-9]{2}\))", "PhD", "Masters"]

MASTERS = "Masters"
PhD = "PhD"

MILLENIA = "20"
SESSION_REGEX = "([S,F])([0-9]{2})"
SESSION_MAP = {
    'F': 'Fall',
    'S': 'Spring'
}



class ProgramParser(object):
    def __init__(self, raw_string):
        self.raw_string = raw_string

    def get_term_year(self):
        return MILLENIA + re.findall(SESSION_REGEX, self.raw_string)[0][1]

    def get_session(self):
        return SESSION_MAP[re.findall(SESSION_REGEX, self.raw_string)[0][0]]

    def get_course_type(self):
        if MASTERS in self.raw_string:
            return MASTERS
        elif PhD in self.raw_string:
            return PhD

    def get_program_name(self):
        return self.__clean_text(self.raw_string)

    def __clean_text(self, text):
        new_text = text
        for rgx_match in UNWANTED_TERMS_IN_COURSE:
            new_text = re.sub(rgx_match, '', new_text)
        return new_text.rstrip(',').strip()